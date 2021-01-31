from creatures.stats.generic_stat import Stat

class ArmorClass (Stat):
  def __init__(self, val=10):
    super().__init__(val)
    self._armor = None
