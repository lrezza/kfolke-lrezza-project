
#Structlike class for representing positions (points) in grid
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Stores an array with four matrices representing a shape with its 4 rotations (states)
class Shape:
    def __init__(self, rotations):
        self.rotations = rotations
        self.rot_state = 0
        pass
    
    def rotate(self):
        self.rot_state += (self.rot_state + 1) % 4

    def get_current(self):
        return self.rotations[self.rot_state]

#Represents the instance of a figure in the scene
class Figure:
    def __init__(self, shape, pos):
        self.shape = shape
        self.shape.rot_state = 0
        self.pos = pos
        pass

