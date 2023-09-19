from dataclasses import dataclass
from typing import Optional

from .UserPreview import User
from .Stamp import Stamp


@dataclass
class BasicComment:
    id: int
    comment: str
    has_replies: bool
    date: str
    user: User
    stamp: Optional[Stamp] = None


@dataclass
class Comment(BasicComment):
    parent_comment: Optional[BasicComment] = None
