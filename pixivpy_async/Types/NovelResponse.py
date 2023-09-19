from dataclasses import dataclass, field

from .Novel import Novel, NovelSeriesDetail
from .UserPreview import User


@dataclass
class BasicListNovelResponse:
    novels: list[Novel] = field(default_factory=list)
    next_url: str | None = None


@dataclass
class ListNovelSeriesResponse(BasicListNovelResponse):
    novel_series_detail: NovelSeriesDetail | None = None
    novel_series_first_novel: Novel | None = None
    novel_series_latest_novel: Novel | None = None


@dataclass
class NovelTextResponse:
    novel_text: str
    novel_marker: dict
    series_prev: Novel = field(default_factory=dict)
    series_next: Novel = field(default_factory=dict)


@dataclass
class ListUserNovelsResponse(BasicListNovelResponse):
    user: User = field(default_factory=User)


@dataclass
class SearchNovelResponse(BasicListNovelResponse):
    search_span_limit: int = 0
    show_ai: bool = False
