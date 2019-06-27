class Cell:

    def __init__s(self, data):
        self.value = data
        self.left = None
        self.right = None

    def __str__(self):
        return '%s' % self.value

    def __repr__(self):
        return 'Cell(%s, %s, %s)' % (self.left, self.value, self.right)
