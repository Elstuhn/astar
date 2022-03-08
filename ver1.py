class Node:
    def __init__(self, parent = None, position = None):
        self.g = self.h = self.f = 0
        self.parent = parent
        self.pos = position
        
    def __eq__(self, node):
        return self.pos == node.pos

def find_path(map):
    pass