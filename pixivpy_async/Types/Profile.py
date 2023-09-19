from dataclasses import dataclass


@dataclass
class Profile:
    webpage: str = ""
    gender: str = ""
    birth: str = ""
    region: str = ""
    job: str = ""
    total_follow_users: int = 0
    total_follower: int = 0
    total_mypixiv_users: int = 0
    total_illusts: int = 0
    total_manga: int = 0
    total_novels: int = 0
    total_illust_bookmarks_public: int = 0
    background_image_url: str = ""
    twitter_account: str = ""
    twitter_url: str = ""
    is_premium: bool = False