
class StatOutOfBoundsError (Exception):
	def __init__(self, text):
		super().__init__(text)
		
if __name__ == '__main__':
	raise StatOutOfBoundError('str can be 20 maximum')
