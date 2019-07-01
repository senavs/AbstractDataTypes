class Node(object):
    
    REPR_FMT = "Node: %s\nValue: %s\nLeft child: %s\nRight Child: %s"
    
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.left = None
        self.right = None
        
    def add(self, node):
        if node.key < self.key:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        elif node.key > self.key:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)
                   
    def visit(self):
        if self.left is not None:
            self.left.visit()
        print(self.value)
        if self.right is not None:
            self.right.visit()
    
    def search(self, key):
        if key == self.key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        elif key > self.key and self.right is not None:
            return self.right.search(key)
    
    def psearch(self, key):
        curr = self
        parent = None
        while curr is not None and curr.key != key:
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return curr, parent
       
    def _min_child(self):
        if self.left is None:
            return self
        return self.left._min_child()
    
    def __repr__(self):
        return self.REPR_FMT % (self.key, self.value, self.left, self.right)
    
    def __str__(self):
        return '%s' % self.key
