import asyncio
from ..context import Context, Module
from ..cogs.util import QUEUE_ACTIVE, QUEUE_PROGRESS, QUEUE_CURRENT_USERS, QUEUE_OPEN

from ..db import QueueDao, get_queue_dao
from ..exceptions import NotbotException, UserAlreadyQueued, UserAttacking, QueueNotOpen

MODULE_NAME = "queue_service"


class QueueService(Module):
    def __init__(self, context: Context):
        self.queue_dao = get_queue_dao(context)

    def get_name(self):
        return MODULE_NAME

    async def reset_queue(self, guild_id, queue_name):
        await self.queue_dao.delete_queued_users(guild_id, queue_name)

        for k in [QUEUE_ACTIVE, QUEUE_PROGRESS, QUEUE_CURRENT_USERS]:
            await self.queue_dao.del_key(guild_id, queue_name, k)

    async def clear_queued_users(self, guild_id, queue_name):
        await self.queue_dao.delete_queued_users(guild_id, queue_name)

    async def queue_up(self, user_id, guild_id, queue_name):
        queueconfig, queued_users = await asyncio.gather(
            self.queue_dao.get_queue_configuration(guild_id, queue_name),
            self.queue_dao.get_queued_users(guild_id, queue_name),
            return_exceptions=True,
        )

        current_users = queueconfig.get(QUEUE_CURRENT_USERS, "").split()
        queue_open = int(queueconfig.get(QUEUE_OPEN, 0))

        if not queue_open:
            raise QueueNotOpen()

        if str(user_id) in queued_users:
            raise UserAlreadyQueued(queued_users.index(str(user_id)))
        elif str(user_id) in current_users:
            raise UserAttacking()
        else:
            res = await self.queue_dao.add_user_to_queued_users(
                guild_id, queue_name, user_id
            )
            queued_users.append(user_id)
            if not res:
                raise NotbotException(
                    "Sorry... Something went wrong. Please try to queue up again"
                )

    async def pause_queue(self, guild_id, queue_name):
        await self.queue_dao.pause_queue(guild_id, queue_name)

    async def resume_queue(self, guild_id, queue_name):
        await self.queue_dao.resume_queue(guild_id, queue_name)

    async def open_queue(self, guild_id, queue_name):
        await self.queue_dao.open_queue(guild_id, queue_name)

    async def close_queue(self, guild_id, queue_name):
        await self.queue_dao.close_queue(guild_id, queue_name)


def get_queue_service(context: Context) -> QueueService:
    return context.get_or_register_module(MODULE_NAME, lambda: QueueService(context))
