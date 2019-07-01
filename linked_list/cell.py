class Cell:

	def __init__(self, data):
		self.value = data
		self.next = None
		self.previous = None

	def __repr__(self):
		return 'Cell(%s, %s, %s)' % (self.next, self.value, self.previous)

	def __str__(self):
		return '%s' % self.value
