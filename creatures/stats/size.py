
from enum import Enum

class Size (Enum):
  Tiny = 0
  Small = 1
  Medium = 2
  Large = 3
  Huge = 4
  Gargantuan = 5

  @staticmethod
  def get_side_length(sz):
    s = 5
    if sz == Size.Tiny:
      s = 2.5
    elif sz in [Size.Small, Size.Medium]:
      s = 5
    elif sz == Size.Large:
      s = 10
    elif sz == Size.Huge:
      s = 15
    elif sz == Size.Gargantuan:
      s = 20
    return s
