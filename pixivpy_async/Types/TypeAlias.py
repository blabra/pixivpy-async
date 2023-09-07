from typing import Literal

IllustRankingMode = Literal[
    "day", "week", "month", "day_male", "day_female", "week_original", "week_rookie", "day_manga"]

SearchTarget = Literal["partial_match_for_tags", "exact_match_for_tags", "title_and_caption"]

Restriction = Literal["public", "private"]

ContentType = Literal["illust", "manga"]

DateSort = Literal["date_desc", "date_asc"]

Duration = Literal["within_last_day", "within_last_week", "within_last_month"] | None

EmptyDict = {}

PlatformFilter = Literal["for_ios", "for_android"]  # 设备类型过滤器（可能与谷歌商店和AppStore的审核政策有关，会影响内容的显示）
