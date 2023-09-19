from dataclasses import dataclass

from .UserPreview import User
from .illustration import ImageUrls
from .Tags import NovelTag


@dataclass(frozen=True)
class NovelSeries:
    id: int
    name: str


@dataclass(frozen=True)
class NovelSeriesDetail:
    id: int
    title: str
    caption: str
    is_original: bool
    is_concluded: bool
    content_count: int
    total_character_count: int
    user: User
    display_text: str
    novel_ai_type: int
    watchlist_added: bool


@dataclass(frozen=True)
class Novel:
    id: int
    title: str
    caption: str
    restrict: int
    x_restrict: int
    is_original: bool
    image_urls: ImageUrls
    create_date: str
    tags: list[NovelTag]
    page_count: int
    text_length: int
    user: User
    series: NovelSeries
    is_bookmarked: bool
    total_bookmarks: int
    total_view: int
    visible: bool
    total_comments: int
    is_muted: bool
    is_mypixiv_only: bool
    is_x_restricted: bool
    novel_ai_type: int
    comment_access_control: int
