class Cell:

	def __init__(self, data):
		self.value = data
		self.left = None
		self.right = None

	def __repr__(self):
		return 'Cell(%s, %s, %s)' % (self.left, self.value, self.right)

	def __str__(self):
		return '%s' % self.value
