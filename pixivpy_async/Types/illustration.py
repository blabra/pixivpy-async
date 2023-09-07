from dataclasses import dataclass, field

from .User import User
from .Tags import IllustTag


@dataclass
class ImageUrls:
    square_medium: str = field(default_factory=str)
    medium: str = field(default_factory=str)
    large: str = field(default_factory=str)
    original: str = field(default_factory=str)


@dataclass
class MetaSinglePage:
    original_image_url: str = field(default_factory=str)


@dataclass(frozen=True)
class Illustration:
    id: int = 0
    width: int = 0
    height: int = 0
    sanity_level: int = 0
    total_view: int = 0
    total_bookmarks: int = 0
    restrict: int = 0
    page_count: int = 0
    total_comments: int = 0
    illust_ai_type: int = 0
    illust_book_style: int = 0
    x_restrict: int = 0

    is_bookmarked: bool = False
    visible: bool = False
    is_muted: bool = False

    create_data: str = field(default_factory=str)
    title: str = field(default_factory=str)
    type: str = field(default_factory=str)
    caption: str = field(default_factory=str)

    tools: list[str] = field(default_factory=list)
    tags: list[IllustTag] = field(default_factory=list)
    mata_pages: list[ImageUrls] = field(default_factory=list)
    user: User = field(default_factory=User)
    image_urls: ImageUrls = field(default_factory=ImageUrls)
    meta_single_page: MetaSinglePage = field(default_factory=MetaSinglePage)


# Ugoria

ZipUrls = ImageUrls


@dataclass
class UgoriaFrame:
    file: str
    delay: int


@dataclass
class UgoriaMetadata:
    zip_urls: ZipUrls
    frames: list[UgoriaFrame]