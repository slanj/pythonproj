class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        from math import sqrt
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        dist = sqrt(x_diff_sq + y_diff_sq)
        return dist
    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x
    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Coordinate(new_x, new_y)
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Coordinate(new_x, new_y)
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'
    def __str__(self):
        return str((self.x, self.y))

c = Coordinate(3, 4)
cc = Coordinate(3, 4)
origin = Coordinate(1, 1)
sum_c = c + origin
distance = c.distance(origin)
print(c)
print(origin)
print(distance)
print(sum_c)
print(type(c))
print(type(Coordinate))
print(isinstance(c, Coordinate))
print(isinstance(sum_c, Coordinate))
print(c == origin)
print(c == cc)
print(eval(repr(c)) == c)
