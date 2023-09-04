from dataclasses import dataclass, field

from User import UserPreview
from Tags import TrendingTag


@dataclass
class BasicListUserResponse:
    user_previews: list[UserPreview] = field(default_factory=list)
    next_url: str | None = None


@dataclass
class ListTrendingTagsIllustsResponse:
    trending_tags: list[TrendingTag] = field(default_factory=list)
