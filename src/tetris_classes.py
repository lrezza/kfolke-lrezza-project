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

#Stores an array with up to four arrays of length 4 representing a shape with its rotations (states)
#Each rotationshape with length 4 represents the indices of the four blocks of the shape in a 4x4 matrix
#Example L-shape rotationstate 1: [3, 5, 6, 7] which corresponds to:
# 0 0 0 1   
# 0 1 1 1
# 0 0 0 0
class Shape:
    def __init__(self, rotations, color):
        self.rotations = rotations
        self.rot_state = 0
        self.color = color
    
    #Increments current rotationstate which stores the current rotation
    def rotate(self):
        self.rot_state = (self.rot_state + 1) % len(self.rotations)

    #Decrements current rotationstate, used for reversing rotation in case of collision
    def rotate_back(self):
        self.rot_state = (self.rot_state - 1) % len(self.rotations)

    #Returns current rotation in form of a array with length 4
    def get_current(self):
        return self.rotations[self.rot_state]

#Represents the instance of a figure in the scene
class Figure:
    def __init__(self, shape, pos):
        self.shape = shape
        self.shape.rot_state = 0
        self.pos = pos

    #Checks if current rotationshape collides with anything in the grid
    def check_collision(self, grid):
        height = len(grid)
        width = len(grid[0])
        current_shape = self.shape.get_current()
        block_points = []
        for n in range(4):
            block_point = Point(0, 0)
            block_point.shape_local_to_global(self.pos, current_shape[n])
            if (block_point.y < 0 or block_point.y >= height or          
                block_point.x < 0 or block_point.x >= width or            
                grid[block_point.y][block_point.x] != 0):                  
                return False                                             
        return True

    #Appends the current rotationshape to a grid used for drawing,
    #collision should be checked before drawing
    def draw_shape(self, grid):
        height = len(grid)
        width = len(grid[0])
        current_shape = self.shape.get_current()
        block_points = []
        for n in range(4):
            block_point = Point(0, 0)
            block_point.shape_local_to_global(self.pos, current_shape[n])
            if (0 <= block_point.y and block_point.y < height and           #Make sure x and y coordinate
                0 <= block_point.x and block_point.x < width and            #is within bounds of the grid
                grid[block_point.y][block_point.x] == 0):                   #and the modified value is 
                                                                            #initially = 0
                block_points.append(block_point) 
            else:
                return False
        color = self.shape.color

        for n in range(4):
            block_point = block_points[n]
            grid[block_point.y][block_point.x] = color
        
        return True

#Creating instances of the shapeclass representing the 7 different shapes in tetris
#with their corresponding rotations
shape_L = Shape([[3, 5, 6, 7], [1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11]], 1)
shape_S = Shape([[1, 2, 4, 5], [0, 4, 5, 9], [5, 6, 8, 9], [1, 5, 6, 10]], 2)
shape_J = Shape([[4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 8, 9]], 3)
shape_I = Shape([[4, 5, 6, 7], [1, 5, 9, 13]], 4)
shape_T = Shape([[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], 5)
shape_Z = Shape([[1, 2, 6, 7], [2, 5, 6, 9], [5, 6, 10, 11], [3, 6, 7, 10]], 6)
shape_O = Shape([[1, 2, 5, 6]], 7)

shapes = [shape_L, shape_S, shape_J, shape_I, shape_T, shape_Z, shape_O]


