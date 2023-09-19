from dataclasses import dataclass, field


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
