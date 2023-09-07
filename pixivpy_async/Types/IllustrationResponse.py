from dataclasses import dataclass, field
from typing import Optional

from .illustration import Illustration
from .User import User
from .Comment import Comment
from .TypeAlias import Restriction
from .Tags import BookmarkTag


@dataclass
class BasicListIllustsResponse:
    illusts: list[Illustration] = field(default_factory=list)
    next_url: str | None = None


@dataclass
class SearchIllustResponse(BasicListIllustsResponse):
    search_span_limit: int = 0
    show_ai: bool = False


@dataclass
class ListUserIllustsResponse(BasicListIllustsResponse):
    user: User = field(default_factory=User)


@dataclass
class PrivacyPolicy:
    version: str = ""
    message: str = ""


@dataclass
class ListIllustsRecommendResponse(BasicListIllustsResponse):
    rankin_illusts: list[Illustration] = field(default_factory=list)
    contest_exists: bool = False
    privacy_policy: Optional[PrivacyPolicy] = None


@dataclass
class IllustCommentsResponse:
    total_comments: int
    comments: list[Comment]
    comment_access_control: int
    next_url: str | None = None


@dataclass
class IllustBookmarkDetailsResponse:
    is_bookmarked: bool
    tags: list[BookmarkTag]
    restrict: Restriction
