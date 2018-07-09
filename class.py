class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        import math
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        dist = math.sqrt(x_diff_sq + y_diff_sq)
        return dist

c = Coordinate(3, 4)
origin = Coordinate(0, 0)
distance = c.distance(origin)
print(c.x)
print(origin.x)
print(distance)