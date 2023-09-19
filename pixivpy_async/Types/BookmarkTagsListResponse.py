from dataclasses import dataclass, field

from .BookmarkTagCounter import BookmarkTagCounter


@dataclass
class BookmarkTagsListResponse:
    bookmark_tags: list[BookmarkTagCounter] = field(default_factory=list)
    next_url: str | None = None
