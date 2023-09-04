from dataclasses import dataclass
from User import User


@dataclass
class BasicComment:
    id: int
    comment: str
    date: str
    user: User


@dataclass
class Comment(BasicComment):
    parent_comment: BasicComment
