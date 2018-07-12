class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def intersect(self, other):
        selected = intSet()
        for item in self.vals:
            if other.member(item):
                selected.insert(item)
        return selected
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def __len__(self):
        return len(self.vals)
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return "{" + result[:-1] + '}'

i = intSet()
i.insert(5)
i.insert(5)
i.insert(77)
i.insert(55)
print("intSet i: ", i)

m = intSet()
m.insert(5)
m.insert(55)
print("intSet m: ", m)

im = i.intersect(m)
print(m, " is interselect between i and m")

print("m len is: ", len(m))

i.remove(55)
print("Remove 55 from i:", i)