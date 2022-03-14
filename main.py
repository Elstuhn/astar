from func import *
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

astar(map_, vmap)
