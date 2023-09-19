from dataclasses import dataclass, field

from .User import User
from .Workspace import Workspace
from .Profile import Profile


@dataclass
class UserDetail:
    user: User = field(default_factory=User)
    profile: Profile = field(default_factory=Profile)
    workspace: Workspace = field(default_factory=Workspace)