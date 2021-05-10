
#Structlike class for representing positions (points) in grid
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Stores an array with four matrices representing a shape with its 4 rotations (states)
class Shape:
    def __init__(self, rotations):
        self.rotations = rotations
        pass
        
#Represents the instance of a figure in the scene
class Figure:
    def __init__(self):
        pass

