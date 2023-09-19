from dataclasses import dataclass, field

from .illustration import Illustration
from .Novel import Novel
from .User import User


@dataclass
class UserPreview:
    user: User = field(default_factory=User)
    illusts: list[Illustration] = field(default_factory=list)
    novels: list[Novel] = field(default_factory=list)
    is_muted: bool = False
