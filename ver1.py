### Assuming that each step up/down/left/right is 2 units of distance

import numpy as np
import typing as t

class Node:
    def __init__(self, parent = None, position : tuple = None): # parent is Node
        self.g = self.h = self.f = 0
        self.parent = parent
        self.pos = position

    def updateF(self):
        self.f = self.g + self.h

    def __eq__(self, node):
        return self.pos == node.pos

def astar(map_ : list, numMap : list, start : tuple = (0, 0), end : tuple = (-1, -1)):
    """
    start and end are tuples of node positions
    returns a 2d array containing the optimal path in sequence
    """
    explored = [map_[start[0]][start[1]]]
    cur_node = map_[start[0]][start[1]]
    gtotal = 0
    cur_node.g = gtotal
    cur_node.h = (((start[0] - end[0]) ** 2) + ((start[1] - end[1]) ** 2))
    cur_node.updateF()
    while not cur_node == map_[end[0]][end[1]]:
        gtotal += 2
        explore = []
        position = cur_node.pos
        posX, posY = position

        posChecks = ("map_[posX - 1][posY]", "map_[posX + 1][posY]",
                     "map_[posX][posY - 1]", "map_[posX][posY + 1]")
        lowest = float("inf")
        for position in posChecks:
            try:
                explore.append(eval(position))
            except:
                continue
            node = eval(position)
            if numMap[node.pos[0]][node.pos[1]]:
                node.f = float("inf")
                continue
            elif eval(position) in explored:
                continue
            node.g = gtotal
            node.h = (((node.pos[0] - end[0]) ** 2) + ((node.pos[1] - end[1]) ** 2))
            node.updateF()
            node.parent = cur_node
            if node.f < lowest:
                lowest = node.f
                nextNode = node
        cur_node = nextNode

    return backtrack(cur_node, map_)



def backtrack(end_node : Node, map_) -> list:
    mapsize = np.array(map_).shape
    path = [[-1 for i in range(mapsize[1])] for j in range(mapsize[0])]
    print(path)
    cur_node = end_node
    print(cur_node.pos)
    path[cur_node.pos[0]][cur_node.pos[1]] = 0
    count = 1
    while cur_node.parent:
        cur_node = cur_node.parent
        path[cur_node.pos[0]][cur_node.pos[1]] = count
        count += 1

    return path

mapr = 5
mapc = 7
map_ = [[Node(position = (j, i)) for i in range(mapc)] for j in range(mapr)]
vmap = \
    [
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    ]

print(astar(map_, vmap))
