from dataclasses import dataclass, field

from pixivpy_async.Types import Illustration, Novel


@dataclass
class ProfileImageUrls:
    medium: str = field(default_factory=str)


@dataclass
class User:
    id: int = 0
    name: str = ""
    account: str = ""
    comment: str = ""
    is_followed: bool = False
    profile_image_urls: ProfileImageUrls = field(default_factory=ProfileImageUrls)
    is_access_blocking_user: bool = False


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


@dataclass
class Workspace:
    pc: str = ""
    monitor: str = ""
    tool: str = ""
    scanner: str = ""
    tablet: str = ""
    mouse: str = ""
    printer: str = ""
    desktop: str = ""
    music: str = ""
    desk: str = ""
    chair: str = ""
    comment: str = ""
    workspace_image_url: str = ""


@dataclass
class UserDetail:
    user: User = field(default_factory=User)
    profile: Profile = field(default_factory=Profile)
    workspace: Workspace = field(default_factory=Workspace)


@dataclass
class UserPreview:
    user: User = field(default_factory=User)
    illusts: list[Illustration] = field(default_factory=list)
    novels: list[Novel] = field(default_factory=list)
    is_muted: bool = False
