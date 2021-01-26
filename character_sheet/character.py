from ability_scores import AbilityScores
from alignment import Alignment

class Character(object):
	def __init__(self):
		self._name = None
		self._race = None
		self._class = None
		self._ability_scores = AbilityScores()
		self._level = 1
		self._proficiency_bonus = 2
		self._background = None
		self._size =
		self._languages = []
		
		self._age
		self._alignment = Alignment.LG
		self._ideals = []
		self._bonds = []
		self._flaws = []
		
		
if __name__ == '__main__':
	c = Character()
	print(c._ability_scores)
