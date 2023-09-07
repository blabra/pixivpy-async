from dataclasses import dataclass
from typing import Optional

from .User import User


@dataclass
class Stamp:
    stamp_id: int = 0
    stamp_url: str = ""


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
