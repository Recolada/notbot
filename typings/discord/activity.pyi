"""
This type stub file was generated by pyright.
"""

"""
The MIT License (MIT)

Copyright (c) 2015-2019 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
__all__ = ('Activity', 'Streaming', 'Game', 'Spotify')
class _ActivityTag:
    __slots__ = ...


class Activity(_ActivityTag):
    """Represents an activity in Discord.

    This could be an activity such as streaming, playing, listening
    or watching.

    For memory optimisation purposes, some activities are offered in slimmed
    down versions:

    - :class:`Game`
    - :class:`Streaming`

    Attributes
    ------------
    application_id: :class:`int`
        The application ID of the game.
    name: :class:`str`
        The name of the activity.
    url: :class:`str`
        A stream URL that the activity could be doing.
    type: :class:`ActivityType`
        The type of activity currently being done.
    state: :class:`str`
        The user's current state. For example, "In Game".
    details: :class:`str`
        The detail of the user's current activity.
    timestamps: :class:`dict`
        A dictionary of timestamps. It contains the following optional keys:

        - ``start``: Corresponds to when the user started doing the
          activity in milliseconds since Unix epoch.
        - ``end``: Corresponds to when the user will finish doing the
          activity in milliseconds since Unix epoch.

    assets: :class:`dict`
        A dictionary representing the images and their hover text of an activity.
        It contains the following optional keys:

        - ``large_image``: A string representing the ID for the large image asset.
        - ``large_text``: A string representing the text when hovering over the large image asset.
        - ``small_image``: A string representing the ID for the small image asset.
        - ``small_text``: A string representing the text when hovering over the small image asset.

    party: :class:`dict`
        A dictionary representing the activity party. It contains the following optional keys:

        - ``id``: A string representing the party ID.
        - ``size``: A list of up to two integer elements denoting (current_size, maximum_size).
    """
    __slots__ = ...
    def __init__(self, **kwargs):
        self.state = ...
        self.details = ...
        self.timestamps = ...
        self.assets = ...
        self.party = ...
        self.application_id = ...
        self.name = ...
        self.url = ...
        self.flags = ...
        self.sync_id = ...
        self.session_id = ...
        self.type = ...
    
    def __repr__(self):
        ...
    
    def to_dict(self):
        ...
    
    @property
    def start(self):
        """Optional[:class:`datetime.datetime`]: When the user started doing this activity in UTC, if applicable."""
        ...
    
    @property
    def end(self):
        """Optional[:class:`datetime.datetime`]: When the user will stop doing this activity in UTC, if applicable."""
        ...
    
    @property
    def large_image_url(self):
        """Optional[:class:`str`]: Returns a URL pointing to the large image asset of this activity if applicable."""
        ...
    
    @property
    def small_image_url(self):
        """Optional[:class:`str`]: Returns a URL pointing to the small image asset of this activity if applicable."""
        ...
    
    @property
    def large_image_text(self):
        """Optional[:class:`str`]: Returns the large image asset hover text of this activity if applicable."""
        ...
    
    @property
    def small_image_text(self):
        """Optional[:class:`str`]: Returns the small image asset hover text of this activity if applicable."""
        ...
    


class Game(_ActivityTag):
    """A slimmed down version of :class:`Activity` that represents a Discord game.

    This is typically displayed via **Playing** on the official Discord client.

    .. container:: operations

        .. describe:: x == y

            Checks if two games are equal.

        .. describe:: x != y

            Checks if two games are not equal.

        .. describe:: hash(x)

            Returns the game's hash.

        .. describe:: str(x)

            Returns the game's name.

    Parameters
    -----------
    name: :class:`str`
        The game's name.
    start: Optional[:class:`datetime.datetime`]
        A naive UTC timestamp representing when the game started. Keyword-only parameter. Ignored for bots.
    end: Optional[:class:`datetime.datetime`]
        A naive UTC timestamp representing when the game ends. Keyword-only parameter. Ignored for bots.

    Attributes
    -----------
    name: :class:`str`
        The game's name.
    """
    __slots__ = ...
    def __init__(self, name, **extra):
        self.name = ...
    
    def _extract_timestamp(self, data, key):
        ...
    
    @property
    def type(self):
        """Returns the game's type. This is for compatibility with :class:`Activity`.

        It always returns :attr:`ActivityType.playing`.
        """
        ...
    
    @property
    def start(self):
        """Optional[:class:`datetime.datetime`]: When the user started playing this game in UTC, if applicable."""
        ...
    
    @property
    def end(self):
        """Optional[:class:`datetime.datetime`]: When the user will stop playing this game in UTC, if applicable."""
        ...
    
    def __str__(self):
        ...
    
    def __repr__(self):
        ...
    
    def to_dict(self):
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def __hash__(self):
        ...
    


class Streaming(_ActivityTag):
    """A slimmed down version of :class:`Activity` that represents a Discord streaming status.

    This is typically displayed via **Streaming** on the official Discord client.

    .. container:: operations

        .. describe:: x == y

            Checks if two streams are equal.

        .. describe:: x != y

            Checks if two streams are not equal.

        .. describe:: hash(x)

            Returns the stream's hash.

        .. describe:: str(x)

            Returns the stream's name.

    Attributes
    -----------
    name: :class:`str`
        The stream's name.
    url: :class:`str`
        The stream's URL. Currently only twitch.tv URLs are supported. Anything else is silently
        discarded.
    details: Optional[:class:`str`]
        If provided, typically the game the streamer is playing.
    assets: :class:`dict`
        A dictionary comprising of similar keys than those in :attr:`Activity.assets`.
    """
    __slots__ = ...
    def __init__(self, *, name, url, **extra):
        self.name = ...
        self.url = ...
        self.details = ...
        self.assets = ...
    
    @property
    def type(self):
        """Returns the game's type. This is for compatibility with :class:`Activity`.

        It always returns :attr:`ActivityType.streaming`.
        """
        ...
    
    def __str__(self):
        ...
    
    def __repr__(self):
        ...
    
    @property
    def twitch_name(self):
        """Optional[:class:`str`]: If provided, the twitch name of the user streaming.

        This corresponds to the ``large_image`` key of the :attr:`Streaming.assets`
        dictionary if it starts with ``twitch:``. Typically set by the Discord client.
        """
        ...
    
    def to_dict(self):
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def __hash__(self):
        ...
    


class Spotify:
    """Represents a Spotify listening activity from Discord. This is a special case of
    :class:`Activity` that makes it easier to work with the Spotify integration.

    .. container:: operations

        .. describe:: x == y

            Checks if two activities are equal.

        .. describe:: x != y

            Checks if two activities are not equal.

        .. describe:: hash(x)

            Returns the activity's hash.

        .. describe:: str(x)

            Returns the string 'Spotify'.
    """
    __slots__ = ...
    def __init__(self, **data):
        ...
    
    @property
    def type(self):
        """Returns the activity's type. This is for compatibility with :class:`Activity`.

        It always returns :attr:`ActivityType.listening`.
        """
        ...
    
    @property
    def colour(self):
        """Returns the Spotify integration colour, as a :class:`Colour`.

        There is an alias for this named :meth:`color`"""
        ...
    
    @property
    def color(self):
        """Returns the Spotify integration colour, as a :class:`Colour`.

        There is an alias for this named :meth:`colour`"""
        ...
    
    def to_dict(self):
        ...
    
    @property
    def name(self):
        """:class:`str`: The activity's name. This will always return "Spotify"."""
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def __hash__(self):
        ...
    
    def __str__(self):
        ...
    
    def __repr__(self):
        ...
    
    @property
    def title(self):
        """:class:`str`: The title of the song being played."""
        ...
    
    @property
    def artists(self):
        """List[:class:`str`]: The artists of the song being played."""
        ...
    
    @property
    def artist(self):
        """:class:`str`: The artist of the song being played.

        This does not attempt to split the artist information into
        multiple artists. Useful if there's only a single artist.
        """
        ...
    
    @property
    def album(self):
        """:class:`str`: The album that the song being played belongs to."""
        ...
    
    @property
    def album_cover_url(self):
        """:class:`str`: The album cover image URL from Spotify's CDN."""
        ...
    
    @property
    def track_id(self):
        """:class:`str`: The track ID used by Spotify to identify this song."""
        ...
    
    @property
    def start(self):
        """:class:`datetime.datetime`: When the user started playing this song in UTC."""
        ...
    
    @property
    def end(self):
        """:class:`datetime.datetime`: When the user will stop playing this song in UTC."""
        ...
    
    @property
    def duration(self):
        """:class:`datetime.timedelta`: The duration of the song being played."""
        ...
    
    @property
    def party_id(self):
        """:class:`str`: The party ID of the listening party."""
        ...
    


def create_activity(data):
    ...

