"""
This type stub file was generated by pyright.
"""

from discord.enums import Enum
from typing import Any, Optional

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
__all__ = ('BucketType', 'Cooldown', 'CooldownMapping')
class BucketType(Enum):
    default = ...
    user = ...
    guild = ...
    channel = ...
    member = ...
    category = ...


class Cooldown:
    __slots__ = ...
    def __init__(self, rate, per, type):
        self.rate = ...
        self.per = ...
        self.type = ...
    
    def get_tokens(self, current: Optional[Any] = ...):
        ...
    
    def update_rate_limit(self, current: Optional[Any] = ...):
        ...
    
    def reset(self):
        ...
    
    def copy(self):
        ...
    
    def __repr__(self):
        ...
    


class CooldownMapping:
    def __init__(self, original):
        ...
    
    def copy(self):
        ...
    
    @property
    def valid(self):
        ...
    
    @classmethod
    def from_cooldown(cls, rate, per, type):
        ...
    
    def _bucket_key(self, msg):
        ...
    
    def _verify_cache_integrity(self, current: Optional[Any] = ...):
        ...
    
    def get_bucket(self, message, current: Optional[Any] = ...):
        ...
    
    def update_rate_limit(self, message, current: Optional[Any] = ...):
        ...
    


