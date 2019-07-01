from .node import Node


class Tree(object):
    
    def __init__(self, data):
        self.root = None

        for key, value in data.items():
            self.add(key, value)
    
    def add(self, key, val):
        new_node = Node(key, val)
        if self.root is None:
            self.root = new_node
        else:
            self.root.add(new_node)
    
    def remove(self, key):
        if not self.root:
            return None
        curr, parent = self.root.psearch(key)
        if curr.left is None and curr.right is None:
            if curr != self.root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        elif curr.left and curr.right:
            tmp_node = curr.right._min_child()
            tmp_key = tmp_node.key
            tmp_value = tmp_node.value
            self.remove(tmp_key)
            curr.key = tmp_key
            curr.value = tmp_value                   
        else:
            if curr != self.root:
                if curr.left:
                    tmp_key = curr.left.key
                    tmp_value = curr.left.value
                else:
                    tmp_key = curr.right.key
                    tmp_value = curr.right.value
                self.remove(tmp_key)
                curr.key = tmp_key
                curr.value = tmp_value
            else:
                self.root = curr.left if curr.left else curr.right
    
    def search(self, val):
        if self.root:
            return self.root.search(val)
        return None
        
    def traverse(self):
        if self.root:
            self.root.visit()
        return None
