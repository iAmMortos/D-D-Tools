
class AbilityBonus (object):
	def __init__(self, val, source, condition=lambda: True):
		self._val = val
		self._source = source
		self._condition = condition
		
	@property
	def value(self):
		if self._condition():
			return self._val
		else:
			return 0
		
	
