from dataclasses import dataclass, field


@dataclass
class BookmarkTagCounter:
    count: int
    name: str


@dataclass
class BookmarkTagsListResponse:
    bookmark_tags: list[BookmarkTagCounter] = field(default_factory=list)
    next_url: str | None = None
