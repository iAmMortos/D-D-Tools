
from errors import StatOutOfBoundsError

class AbilityScore (object):
	def __init__(self, name, score, short_name=None):
		self._name = name
		self._short_name = name[:3].upper() if short_name is None else short_name
		self._score = score
		self._score_min = 1
		self._score_max = 20
		
	@property
	def name(self):
		return self._name
		
	@property
	def short_name(self):
		return self._short_name
		
	@property
	def score(self):
		return self._score

	def set_score(self, score, override=False):
		if override or score >= self._score_min and score <= self._score_max:
			self._score = score
		else:
			raise StatOutOfBoundsError('%s stat cannot be outside range [%s - %s]. (%s) given.' % (self.name, self._score_min, self._score_max, score))
			
	@property
	def bonus(self):
		return (self._score - 10) // 2
		
	@property
	def bonus_as_str(self):
		return '%s%s' % ('+' if self.bonus >= 0 else '', self.bonus)
	
	def __repr__(self):
		return '%s (%s): %s (%s)' % (self._name, self._short_name, self._score, self.bonus_as_str)
		

if __name__ == '__main__':
	ab = AbilityScore('Strength', 1)
	print(ab)
	while ab.score < ab._score_max + 1:
		ab.set_score(ab.score + 1)
		print(ab)
