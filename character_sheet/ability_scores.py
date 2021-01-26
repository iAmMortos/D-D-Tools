
from ability_score import AbilityScore
from ability_type import AbilityType

class AbilityScores (object):
	order = [AbilityType.STR, AbilityType.DEX, AbilityType.CON, AbilityType.WIS, AbilityType.INT, AbilityType.CHA]
	presets = [15, 14, 13, 12, 10, 8]
	def __init__(self, as_str=10, as_dex=10, as_con=10, as_wis=10, as_int=10, as_cha=10):
		self._scores = {
			AbilityType.STR: AbilityScore(AbilityType.STR.value, as_str),
			AbilityType.DEX: AbilityScore(AbilityType.DEX.value, as_dex),
			AbilityType.CON: AbilityScore(AbilityType.CON.value, as_con),
			AbilityType.WIS: AbilityScore(AbilityType.WIS.value, as_wis),
			AbilityType.INT: AbilityScore(AbilityType.INT.value, as_int),
			AbilityType.CHA: AbilityScore(AbilityType.CHA.value, as_cha)}
		
	def get_full_ability_str(self):
		return '|'.join(['%s %s(%s)' % (self._scores[a].short_name, self._scores[a].score, self._scores[a].bonus_as_str) for a in AbilityScores.order])
		
	def get_scores_list(self):
		return [self._scores[a].score for a in AbilityScores.order]
		
	def get_scores_str(self):
		return '|'.join(['%s %s' % (self._scores[a].short_name, self._scores[a].score) for a in AbilityScores.order])
		
	def get_bonuses_list(self):
		return [self._scores[a].bonus for a in AbilityScores.order]
		
	def get_bonuses_str(self):
		return '|'.join(['%s %s' % (self._scores[a].short_name, self._scores[a].bonus_as_str) for a in AbilityScores.order])
		
	@property
	def str(self):
		return self._scores[AbilityType.STR].score
	@property
	def str_bonus(self):
		return self._scores[AbilityType.STR].bonus
	@property
	def dex(self):
		return self._scores[AbilityType.DEX].score
	@property
	def dex_bonus(self):
		return self._scores[AbilityType.DEX].bonus
	@property
	def con(self):
		return self._scores[AbilityType.CON].score
	@property
	def con_bonus(self):
		return self._scores[AbilityType.CON].bonus
	@property
	def wis(self):
		return self._scores[AbilityType.WIS].score
	@property
	def wis_bonus(self):
		return self._scores[AbilityType.WIS].bonus
	@property
	def int(self):
		return self._scores[AbilityType.INT].score
	@property
	def int_bonus(self):
		return self._scores[AbilityType.INT].bonus
	@property
	def cha(self):
		return self._scores[AbilityType.CHA].score
	@property
	def cha_bonus(self):
		return self._scores[AbilityType.CHA].bonus
		
	def get_score(self, ability):
		return self._scores[ability].score
	
	def get_bonus(self, ability):
		return self._scores[ability].bonus
		
	def set_score(self, type, value, override=False):
		self._scores[type].set_score(value, override=override)
		
	def copy_scores_from(self, other_scores):
		for t in AbilityScores.order:
			self.set_score(t, other_scores.get_score(t), override=True)
		
	def __repr__(self):
		return self.get_full_ability_str()
		
if __name__ == '__main__':
	a = AbilityScores(*AbilityScores.presets)
	a.set_score(AbilityType.CHA, 12)
	print(a)
