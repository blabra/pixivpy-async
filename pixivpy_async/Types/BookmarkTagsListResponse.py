from .BookmarkTagCounter import *


@dataclass
class BookmarkTagsListResponse:
    bookmark_tags: list[BookmarkTagCounter] = field(default_factory=list)
    next_url: str | None = None
