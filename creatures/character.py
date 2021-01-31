
from creatures.creature import Creature

class Character (Creature):
  def __init__(self):
    super().__init__()
    self._race = None
    self._classes = []
