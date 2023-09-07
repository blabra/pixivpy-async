# -*- coding:utf-8 -*-
from .bapi import BasePixivAPI

from .Types import *
from .additional_functions import to_dataclass


# App-API (6.x - app-api.pixiv.net)


class AppPixivAPI(BasePixivAPI):
    def __init__(self, **requests_kwargs):
        """
        initialize requests kwargs if need be
        """
        super(AppPixivAPI, self).__init__(**requests_kwargs)

    async def user_detail(
            self,
            user_id: int = 660788,
            filter: PlatformFilter = 'for_ios',
            req_auth: bool = True
    ) -> UserDetail:
        """
        获取用户详情

        PARAMETERS:
            user_id(int): 查询的目标用户ID
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            UserDetail(Dataclass)
        """
        method, url = self.api.user_detail
        params = self.set_params(
            user_id=user_id,
            filter=filter
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(UserDetail, result)

    async def user_illusts(
            self,
            user_id: int,
            type: Literal["illust", "manga"] = 'illust',
            filter: PlatformFilter = 'for_ios',
            offset: int = None,
            req_auth: bool = True
    ) -> ListUserIllustsResponse:
        """
        获取用户的作品列表

        PARAMETERS:
            user_id(int): 查询的目标用户ID
            type(str): 查询的作品类型。illust -> 插画，manga -> 漫画
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            offset(int | None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            BasicListIllustsResponse(Dataclass)
        """
        method, url = self.api.user_illusts
        params = self.set_params(
            user_id=user_id,
            filter=filter,
            type=type,
            offset=offset
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(ListUserIllustsResponse, result)

    async def user_bookmarks_illust(
            self,
            user_id: int,
            restrict: Restriction = 'public',
            filter: PlatformFilter = 'for_ios',
            max_bookmark_id: int = None,
            tag: str = None,
            req_auth: bool = True
    ) -> BasicListIllustsResponse:
        """
        获取用户的作品收藏列表

        PARAMETERS:
            user_id(int): 查询的目标用户ID
            restrict(str): 查询的关注列表类型。public -> 公开关注列表, private -> 秘密关注列表
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            max_bookmark_id(int): 最大作品收藏ID
            tag(str):  从 user_bookmark_tags_illust 获取的收藏标签
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            BasicListIllustsResponse(Dataclass)
        """
        method, url = self.api.user_bookmarks_illust
        params = self.set_params(
            user_id=user_id,
            filter=filter,
            restrict=restrict,
            max_bookmark_id=max_bookmark_id,
            tag=tag
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(BasicListIllustsResponse, result)

    async def user_related(
            self,
            seed_user_id: int,
            filter: PlatformFilter = 'for_ios',
            offset: int = None,
            req_auth: bool = True
    ) -> BasicListUserResponse:
        """
        获取目标用户的相关用户

        PARAMETERS:
            seed_user_id(int): 目标用户ID
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            offset(int | None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            BasicListIllustsResponse(Dataclass)
        """
        method, url = self.api.user_related
        params = self.set_params(
            seed_user_id=seed_user_id,
            filter=filter,
            offset=offset
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(BasicListUserResponse, result)

    async def illust_follow(
            self,
            restrict: Restriction = 'public',
            offset: int = None,
            req_auth: bool = True
    ) -> BasicListIllustsResponse:
        """
        获取关注用户的新作，需登录

        PARAMETERS:
            restrict(str): 查询的关注用户列表类型。public -> 公开关注列表, private -> 秘密关注列表
            offset(int|None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            BasicListIllustsResponse(Dataclass)
        """
        method, url = self.api.illust_follow
        params = self.set_params(
            restrict=restrict,
            offset=offset
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(BasicListIllustsResponse, result)

    async def illust_detail(
            self,
            illust_id: int,
            req_auth: bool = True
    ) -> Illustration:
        """
        获取作品的详细信息(类似PAPI.works()，iOS中未使用)

        PARAMETERS:
            illust_id(int): 作品ID
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            Illustration(Dataclass)
        """
        method, url = self.api.illust_detail
        params = self.set_params(
            illust_id=illust_id
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(Illustration, result["illust"])

    async def illust_comments(
            self,
            illust_id: int,
            offset: int = None,
            include_total_comments=None,
            req_auth: bool = True
    ) -> IllustCommentsResponse:
        """
        获取作品的评论

        PARAMETERS:
            illust_id(int): 作品ID
            include_total_comments(Unknown): Unknown
            offset(int|None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            IllustCommentsResponse(Dataclass)
        """
        method, url = self.api.illust_comments
        params = self.set_params(
            illust_id=illust_id,
            offset=offset,
            include_total_comments=include_total_comments
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(IllustCommentsResponse, result)

    async def illust_related(
            self,
            illust_id: int,
            filter: PlatformFilter = 'for_ios',
            seed_illust_ids: list = None,
            offset: int = None,
            req_auth: bool = True
    ) -> BasicListIllustsResponse:
        """
        相关作品列表

        PARAMETERS:
            illust_id(int): 需查找相关作品的插画 ID
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            seed_illust_ids(list): Unknown
            offset(int|None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            ListIllustsRecommendResponse(Dataclass)
        """
        method, url = self.api.illust_related
        params = self.set_params(
            illust_id=illust_id,
            offset=offset,
            filter=filter,
            seed_illust_ids=seed_illust_ids,
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(BasicListIllustsResponse, result)

    async def illust_recommended(
            self,
            content_type: ContentType = 'illust',
            include_ranking_label: bool = True,
            filter: PlatformFilter = 'for_ios',
            max_bookmark_id_for_recommend: int = None,
            min_bookmark_id_for_recent_illust: int = None,
            offset: int = None,
            include_ranking_illusts: bool = True,
            bookmark_illust_ids: list = None,
            include_privacy_policy: bool = False,
            req_auth: bool = True,
            viewed: list = None
    ) -> ListIllustsRecommendResponse:
        """
        插画推荐 (Home - Main)

        PARAMETERS:
            content_type(str): 稿件类型，可选 illust | manga
            include_ranking_label(bool): 是否包含排名标签
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            max_bookmark_id_for_recommend(int): 用于生成插画推荐的最大插画收藏ID
            min_bookmark_id_for_recent_illust(int): 用于生成最近插画推荐的最小插画收藏ID
            include_ranking_illusts(Undefined): 是否包含排行榜上的插画？
            bookmark_illust_ids(list[str]): Unknown
            include_privacy_policy(bool): 响应体是否包含隐私政策内容
            offset(int|None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。
            viewed(list[str]): 已看过的插画列表？

        RETURNS:
            ListIllustsRecommendResponse(Dataclass)
        """
        if req_auth:
            method, url = self.api.illust_recommended_auth
        else:
            method, url = self.api.illust_recommended_no_auth
        params = self.set_params(
            content_type=content_type,
            offset=offset,
            filter=filter,
            viewed=viewed,
            bookmark_illust_ids=bookmark_illust_ids,
            include_ranking_illusts=include_ranking_illusts,
            include_ranking_label=include_ranking_label,
            include_privacy_policy=include_privacy_policy,
            max_bookmark_id_for_recommend=max_bookmark_id_for_recommend,
            min_bookmark_id_for_recent_illust=min_bookmark_id_for_recent_illust,
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(ListIllustsRecommendResponse, result)

    # 作品排行
    # mode: [day, week, month, day_male, day_female, week_original, week_rookie, day_manga]
    # date: '2016-08-01'
    # mode (Past): [day, week, month, day_male, day_female, week_original, week_rookie,
    #               day_r18, day_male_r18, day_female_r18, week_r18, week_r18g]
    async def illust_ranking(
            self,
            mode: IllustRankingMode = 'day',
            filter: PlatformFilter = 'for_ios',
            date: str = None,
            offset: int = None,
            req_auth: bool = True
    ) -> BasicListIllustsResponse:
        """
        作品排行
        PARAMETERS:
            mode(str): 作品排行榜，可选【day, week, month, day_male, day_female, week_original, week_rookie, day_manga】
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            date(str): 榜单日期，'2016-08-01'
            offset(int|None): 距离搜索请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。
        RETURNS:
            BasicListIllustsResponse(Dataclass)
        """
        method, url = self.api.illust_ranking
        params = self.set_params(
            date=date,
            offset=offset,
            filter=filter,
            mode=mode
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(BasicListIllustsResponse, result)

    # 趋势标签 (Search - tags)
    async def trending_tags_illust(
            self,
            filter: PlatformFilter = 'for_ios',
            req_auth: bool = True
    ) -> ListTrendingTagsIllustsResponse:
        method, url = self.api.trending_tags_illust
        params = self.set_params(
            filter=filter
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(ListTrendingTagsIllustsResponse, result)

    async def search_illust(
            self,
            word: str,
            search_target: SearchTarget = 'partial_match_for_tags',
            sort: Literal['date_desc', 'date_asc'] = 'date_desc',
            duration: Duration = None,
            filter: PlatformFilter = 'for_ios',
            offset: int = None,
            req_auth: bool = True,
            start_date: str = None,
            end_date: str = None,
            min_bookmarks: int = None,
            max_bookmarks: int = None
    ) -> BasicListIllustsResponse:
        """
        搜索图画稿件
        PARAMETERS:
            word(str): 搜索词，必需项。
            search_target(str): 搜索类型，partial_match_for_tags -> 标签部分一致. exact_match_for_tags -> 标签完全一致
                                        title_and_caption -> 标题和说明
            sort(str): 日期排序，默认最新发布在前
            duration(str): 稿件日期范围。within_last_day -> 一天内， within_last_week -> 一周内， within_last_month -> 一个月内，
                                      None -> 不限
            start_date(str): 开始日期， 格式 2020-06-01
            end_date(str): 截止日期， 格式 2020-06-01
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            offset(int|None): 距离搜索请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。
            min_bookmarks(int | None): 最低收藏量要求
            max_bookmarks(int | None): 最大收藏量要求
        RETURNS:
            BasicListIllustsResponse(Dataclass)
        """
        method, url = self.api.search_illust
        params = self.set_params(
            word=word,
            search_target=search_target,
            sort=sort,
            filter=filter,
            duration=duration,
            offset=offset,
            start_date=start_date,
            end_date=end_date,
            bookmark_num_min=min_bookmarks,
            bookmark_num_max=max_bookmarks,
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(BasicListIllustsResponse, result)

    async def illust_bookmark_detail(
            self,
            illust_id: int,
            req_auth: bool = True
    ) -> IllustBookmarkDetailsResponse:
        """
        显示某个稿件的收藏详情

        PARAMETERS:
            illust_id(int): 稿件的 ID
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            Illustration(Dataclass)
        """
        method, url = self.api.illust_bookmark_detail
        params = self.set_params(
            illust_id=illust_id
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)

        if "bookmark_detail" in result:
            return to_dataclass(IllustBookmarkDetailsResponse, result)

    async def illust_bookmark_add(
            self,
            illust_id: int,
            restrict: Restriction = 'public',
            tags: list[str] = None,
            req_auth: bool = True
    ) -> EmptyDict:
        """
        收藏某个稿件

        PARAMETERS:
            illust_id(int): 需要收藏的稿件的 ID
            restrict(str): 添加到公开收藏列表还是秘密收藏列表
            tags(list[str]): 对稿件的收藏标签, 最多10个
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            EmptyDict(一个空字典)
        """
        method, url = self.api.illust_bookmark_add
        data = self.set_params(
            illust_id=illust_id,
            restrict=restrict,
            tags=tags
        )
        return await self.requests_(method=method, url=url, data=data, auth=req_auth)

    async def illust_bookmark_delete(
            self,
            illust_id: int = None,
            req_auth: bool = True
    ) -> EmptyDict:
        """
        取消对某个稿件的收藏

        PARAMETERS:
            illust_id(int): 需要取消收藏的稿件的 ID
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            EmptyDict(一个空字典)
        """
        method, url = self.api.illust_bookmark_delete
        data = self.set_params(
            illust_id=illust_id
        )
        return await self.requests_(method=method, url=url, data=data, auth=req_auth)

    # 关注用户
    async def user_follow_add(
            self,
            user_id: int,
            restrict: Restriction = 'public',
            req_auth: bool = True
    ) -> EmptyDict:
        """
        关注某个用户

        PARAMETERS:
            user_id(int): 需要关注的用户的 ID
            restrict(str): 添加到公开关注列表还是秘密关注列表
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            EmptyDict(一个空字典)
        """
        method, url = self.api.user_follow_add
        data = self.set_params(
            user_id=user_id,
            restrict=restrict
        )
        return await self.requests_(method=method, url=url, data=data, auth=req_auth)

    # 取消关注用户
    async def user_follow_del(
            self,
            user_id: int,
            req_auth: bool = True
    ) -> EmptyDict:
        """
        取消关注某个用户

        PARAMETERS:
            user_id(int): 需要取消关注的用户的 ID
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            EmptyDict(一个空字典)
        """
        method, url = self.api.user_follow_del
        data = self.set_params(
            user_id=user_id,
        )
        return await self.requests_(method=method, url=url, data=data, auth=req_auth)

    # 用户收藏标签列表
    async def user_bookmark_tags_illust(
            self,
            restrict: Restriction = 'public',
            offset: int = None,
            req_auth: bool = True
    ) -> BookmarkTagsListResponse:
        """
        列出登录用户的收藏标签列表

        PARAMETERS:
            restrict(str): 查询的用户列表，public -> 公开关注列表, private -> 秘密关注列表
            offset(int | None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            BookmarkTagsListResponse(Dataclass)
        """
        method, url = self.api.user_bookmark_tags_illust
        params = self.set_params(
            restrict=restrict,
            offset=offset
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        if "bookmark_tags" in result:
            result = result["bookmark_tags"]
        return result

    async def user_following(
            self,
            user_id: int,
            restrict: Restriction = 'public',
            offset: int = None,
            req_auth: bool = True
    ) -> BasicListUserResponse:
        """
        列出正在关注的用户

        PARAMETERS:
            user_id(int): 目标用户 id， 必需项。
            restrict(str): 查询的用户列表，public -> 公开关注列表, private -> 秘密关注列表
            offset(int | None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            BasicListUserResponse
        """
        method, url = self.api.user_following
        params = self.set_params(
            restrict=restrict,
            offset=offset,
            user_id=user_id
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(BasicListUserResponse, result)

    async def user_follower(
            self,
            user_id: int,
            filter: PlatformFilter = 'for_ios',
            offset: int = None,
            req_auth: bool = True
    ) -> BasicListUserResponse:
        """
        列出关注目标用户的用户

        PARAMETERS:
            user_id(int): 目标用户 id， 必需项。
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            offset(int | None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            BasicListUserResponse
        """
        method, url = self.api.user_follower
        params = self.set_params(
            filter=filter,
            offset=offset,
            user_id=user_id
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(BasicListUserResponse, result)

    async def user_mypixiv(
            self,
            user_id: int,
            offset: int = None,
            req_auth: bool = True
    ) -> BasicListUserResponse:
        """
        获取目标用户的好P友列表

        PARAMETERS:
            user_id(str): 目标用户 ID，必需项。
            offset(int | None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            BasicListUserResponse(Dataclass)
        """
        method, url = self.api.user_mypixiv
        params = self.set_params(
            offset=offset,
            user_id=user_id
        )

        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        if "user_previews" in result:
            return to_dataclass(BasicListUserResponse, result)

    async def user_list(
            self,
            user_id: int,
            filter: PlatformFilter = 'for_ios',
            offset: int = None,
            req_auth: bool = True
    ) -> ListBlockedUserResponse:
        """
        获取目标用户纳入黑名单的用户列表

        PARAMETERS:
            user_id(str): 目标用户 ID，必需项。
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            offset(int | None): 距离请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            Undefined
        """
        method, url = self.api.user_list
        params = self.set_params(
            filter=filter,
            offset=offset,
            user_id=user_id
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        if "blocked_users" in result:
            return to_dataclass(ListBlockedUserResponse, result["blocked_users"])

    async def ugoira_metadata(
            self,
            illust_id: int,
            req_auth: bool = True
    ) -> UgoriaMetadata | None:
        """
        获取 ugoira 动图稿件信息

        PARAMETERS:
            illust_id(str): ugoria稿件id，必需项。
            req_auth(bool): 访问请求是否需登录，该请求需要。
        RETURNS:
            UgoriaMetadata(Dataclass)

        """
        method, url = self.api.ugoira_metadata
        params = self.set_params(
            illust_id=illust_id
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        if "ugoira_metadata" in result:
            result = to_dataclass(UgoriaMetadata, result["ugoria_metadata"])
        return result

    async def search_user(
            self,
            word: str,
            sort: DateSort = 'date_desc',
            duration=None,
            filter: PlatformFilter = 'for_ios',
            offset: int | None = None,
            req_auth: bool = True
    ) -> BasicListUserResponse:
        """
        搜索用户

        PARAMETERS:
            word(str): 搜索词，必需项。
            sort(str): 日期排序，默认最新发布在前
            duration(Undefined): 待测试
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            offset(int | None): 距离搜索请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            ListNovelSeriesResponse(Dataclass)
        """
        method, url = self.api.search_user
        params = self.set_params(
            word=word,
            sort=sort,
            filter=filter,
            duration=duration,
            offset=offset
        )

        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        return to_dataclass(BasicListUserResponse, result)

    async def search_novel(
            self,
            word: str,
            search_target: SearchTarget = 'partial_match_for_tags',
            sort: DateSort = 'date_desc',
            merge_plain_keyword_results: Literal["true", "false"] = 'true',
            include_translated_tag_results: Literal["true", "false"] = 'true',
            start_date: str = None,
            end_date: str = None,
            filter: str = None,
            offset: int = None,
            req_auth: bool = True
    ) -> SearchNovelResponse:
        """
        搜索小说

        PARAMETERS:
            word(str): 搜索词，必需项。
            search_target(str): 搜索类型，partial_match_for_tags -> 标签部分一致. exact_match_for_tags -> 标签完全一致
                                        text -> 正文. keyword -> 关键词
            sort(str): 日期排序，默认最新发布在前
            merge_plain_keyword_results(str): 合并纯关键词结果？
            include_translated_tag_results(str)：搜索结果包括翻译后的标签（同时搜索翻译后的标签）
            start_date(str): 开始日期， 格式 2020-06-01
            end_date(str): 截止日期， 格式 2020-06-01
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            offset(int|None): 距离搜索请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            ListNovelSeriesResponse(Dataclass)
        """
        method, url = self.api.search_novel
        params = self.set_params(
            word=word,
            sort=sort,
            filter=filter,
            search_target=search_target,
            merge_plain_keyword_results=merge_plain_keyword_results,
            include_translated_tag_results=include_translated_tag_results,
            start_date=start_date,
            end_date=end_date,
            offset=offset
        )
        return await self.requests_(method=method, url=url, params=params, auth=req_auth)

    async def user_novels(
            self,
            user_id: int,
            filter: PlatformFilter = 'for_ios',
            offset: int = None,
            req_auth: bool = True
    ) -> ListUserNovelsResponse:
        """
        获取用户投稿的小说

        PARAMETERS:
            user_id: 目标用户ID。
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            offset(int|None): 距离搜索请求结果排第一的结果的距离。为 None 时表示从零开始取得，为 1 时表示从第二个请求结果开始取得，以此类推。
                              不可以填0。
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            ListUserNovelsResponse(Dataclass)
        """
        method, url = self.api.user_novels
        params = self.set_params(
            user_id=user_id,
            filter=filter,
            offset=offset
        )
        return await self.requests_(method=method, url=url, params=params, auth=req_auth)

    async def novel_follow(
            self,
            req_auth: bool = True,
            restrict: str = 'all',
            offset: int | None = None
    ):
        """
            返回已关注用户的新小说。最多30个项目。

            restrict(int): 返回内容的限制。可以是 'all', 'public' or 'private'。public表示非R18且非R18G，private表示R18或R18G，all表示二者全部。

            offset(int|None): 距离最新的小说的距离。为None时表示从最新的小说开始取得，为1时表示从第二新的小说开始取得，以此类推。不可以填0。
        """
        method, url = self.api.novel_follow
        params = self.set_params(
            restrict=restrict,
            offset=offset
        )

        return await self.requests_(method=method, url=url, params=params, auth=req_auth)

    async def novel_new(
            self,
            filter: str = 'for_ios',
            max_novel_id: int | str | None = None,
            req_auth: bool = True
    ):
        method, url = self.api.novel_new
        params = self.set_params(
            filter=filter,
            max_novel_id=max_novel_id
        )

        return await self.requests_(method=method, url=url, params=params, auth=req_auth)

    async def novel_series(
            self,
            series_id: int,
            filter: PlatformFilter = 'for_ios',
            last_order=None,
            req_auth: bool = True
    ) -> ListNovelSeriesResponse:
        """
        获取小说系列的详细信息

        PARAMETERS:
            series_id(int): 小说系列的ID，必需项。
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            last_order: 可选项
            req_auth(bool): 访问请求是否需登录，该请求需要。

        RETURNS:
            ListNovelSeriesResponse(Dataclass)
        """
        method, url = self.api.novel_series
        params = self.set_params(
            series_id=series_id,
            filter=filter,
            last_order=last_order
        )
        return await self.requests_(method=method, url=url, params=params, auth=req_auth)

    async def novel_detail(
            self,
            novel_id: int,
            req_auth: bool = True
    ) -> Novel:
        """
        获取小说的详细信息
        PARAMETERS:
            novel_id(int): 小说ID，必选项。
            req_auth(bool): 访问请求是否需登录，该请求需要。
        RETURNS:
            Novel(Dataclass)
        """
        method, url = self.api.novel_detail
        params = self.set_params(
            novel_id=novel_id,
        )
        return await self.requests_(method=method, url=url, params=params, auth=req_auth)

    # 小说正文
    async def novel_text(
            self,
            novel_id: int,
            req_auth: bool = True
    ) -> NovelTextResponse:
        """
        返回小说正文

        PARAMETERS:
            novel_id(int): 目标小说ID
            req_auth(bool): 访问请求是否需登录，该请求需要。

        Returns:
            BasicListNovelResponse(Dataclass) => Dataclass(novels: list[Novel], next_url: string)
        """
        method, url = self.api.novel_text
        params = self.set_params(
            novel_id=novel_id,
        )
        result = await self.requests_(method=method, url=url, params=params, auth=req_auth)
        if "novel_text" in result:
            return to_dataclass(NovelTextResponse, result)

    async def illust_new(
            self,
            content_type: ContentType = "illust",
            filter: PlatformFilter = 'for_ios',
            max_illust_id: int = None,
            req_auth: bool = True
    ):
        """
        返回 P站站内最新投稿的插画/漫画列表

        PARAMETERS:
            content_type(str): 稿件类型, illust -> 插画，manga -> 漫画
            filter(str): 依据设备类型的内容过滤器（可能与谷歌商店和AppStore的审核政策有关，可能会影响内容的显示）
            max_illust_id(int|str): 限制请求的最大 稿件ID
            req_auth(bool): 访问请求是否需登录，该请求需要。

        Returns:
            BasicListNovelResponse(Dataclass) => Dataclass(novels: list[Novel], next_url: string)
        """
        method, url = self.api.illust_new
        params = self.set_params(
            content_type=content_type,
            max_illust_id=max_illust_id,
            filter=filter,
        )
        return await self.requests_(method=method, url=url, params=params, auth=req_auth)

    # 特辑详情 (无需登录，调用Web API)
    async def showcase_article(
            self,
            showcase_id: int,
            req_auth: bool = False
    ):
        method, url = self.api.showcase_article
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36',
            'Referer': 'https://www.pixiv.net',
        }
        params = self.set_params(
            showcase_id=showcase_id
        )

        return await self.requests_(method=method, url=url, headers=headers, params=params, auth=req_auth)
