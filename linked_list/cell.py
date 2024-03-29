class Cell:

    def __init__(self, data):
        self.value = data
        self.next = None

    def __repr__(self):
        return "Cell(%s, %s)" % (self.value, self.next)

    def __str__(self):
        return "%s" % (self.value)
