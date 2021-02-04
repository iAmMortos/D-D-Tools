
from enum import Enum


class ModifierType(Enum):
  ADD = "additive"
  MUL = "multiplicative"


class Modifier (object):
  def __init__(self, val, source, mod_type=ModifierType.ADD):
    self.value = val
    self.source = source
    self.parent = None
    self.mod_type
    
  def remove_from_parent(self):
    self.parent.remove(self)
