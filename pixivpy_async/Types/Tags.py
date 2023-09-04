from dataclasses import dataclass, field
from illustration import Illustration


@dataclass
class IllustTag:
    name: str = field(default_factory=str)
    translated_name: str = field(default_factory=str)


@dataclass
class NovelTag(IllustTag):
    added_by_uploaded_user: bool = False


@dataclass
class BookmarkTag:
    name: str
    is_registered: bool


@dataclass
class TrendingTag(IllustTag):
    illust: Illustration = field(default_factory=Illustration)
