class Cell:

	def __init__(self, data):
		self.value = data
		self.bellow = None

	def __repr__(self):
		return 'Cell(%s, %s)' % (self.value, self.bellow)

	def __str__(self):
		return '%s' % self.value
