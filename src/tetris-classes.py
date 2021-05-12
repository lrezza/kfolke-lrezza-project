import math

#Structlike class for representing positions (points) in grid
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Takes a parent point(figure pos) and a local integer representing a position of a block in a shape, and
    #converts into global grid point
    def shape_local_to_global(self, parent, local):
        self.x = parent.x + (local % 4)
        self.y = parent.y + math.floor(local / 4)

#Stores an array with up to four arrays representing a shape with its rotations (states)
class Shape:
    def __init__(self, rotations, color):
        self.rotations = rotations
        self.rot_state = 0
        self.color = color
    
    def rotate(self):
        self.rot_state = (self.rot_state + 1) % len(self.rotations)

    def get_current(self):
        return self.rotations[self.rot_state]

#Represents the instance of a figure in the scene
class Figure:
    def __init__(self, shape, pos):
        self.shape = shape
        self.shape.rot_state = 0
        self.pos = pos
    
    def draw_shape(self, grid):
        height = len(grid)
        width = len(grid[0])
        current_shape = self.shape.get_current()
        block_points = []
        for n in range(4):
            block_point = Point(0, 0).shape_local_to_global(self.pos, current_shape[n])
            if grid[block_point.x][block_point.y] == 0:
                block_points[n] = block_point
            else:
                return False
        color = self.shape.color

        for n in range(4):
            block_point = block_points[n]
            grid[block_point.x][block_point.y] = color
        
        return True

shape_L = Shape([[3, 5, 6, 7], [1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11]], 1)
shape_S = Shape([[1, 2, 4, 5], [0, 4, 5, 9], [5, 6, 8, 9], [1, 5, 6, 10]], 2)
shape_J = Shape([[4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 8, 9]], 3)
shape_I = Shape([[4, 5, 6, 7], [1, 5, 9, 13]], 4)
shape_T = Shape([[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], 5)
shape_Z = Shape([[1, 2, 6, 7], [2, 5, 6, 9], [5, 6, 10, 11], [3, 6, 7, 10]], 6)
shape_O = Shape([[1, 2, 5, 6]], 7)

shapes = [shape_L, shape_S, shape_J, shape_I, shape_T, shape_Z, shape_O]


