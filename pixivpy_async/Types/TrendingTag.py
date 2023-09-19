from dataclasses import dataclass, field

from .Tags import IllustTag
from .illustration import Illustration


@dataclass
class TrendingTag(IllustTag):
    illust: Illustration = field(default_factory=Illustration)