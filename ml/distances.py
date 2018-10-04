import pylab

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)

class Animal(object):
    def __init__(self, name, features):
        """Assumes name a string; features a list of numbers"""
        self.name = name
        self.features = pylab.array(features)

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self, other):
        """Assumes other an Animal
           Returns the Euclidean distance between feature vectors
              of self and other"""
        return minkowskiDist(self.getFeatures(),
                             other.getFeatures(), 2)

    def __str__(self):
        return self.name

cobra = Animal('cobra', [1,1,1,1,0])
rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa constrictor', [0,1,0,1,0])
chicken = Animal('chicken', [1,1,0,1,2])
alligator = Animal('alligator', [1,1,0,1,4])
dartFrog = Animal('dart frog', [1,0,1,0,4])
salmon = Animal('salmon', [1,1,0,1,0])
python = Animal('python', [1,1,0,1,0])
animals = [cobra, rattlesnake, boa, chicken,
           alligator, dartFrog, salmon, python]

def compareAnimals(animals, precision):
   """Assumes animals is a list of animals, precision an int >= 0
      Builds a table of Euclidean distance between each animal"""
   #Get labels for columns and rows
   columnLabels = []
   for a in animals:
       columnLabels.append(a.getName())
   rowLabels = columnLabels[:]
   tableVals = []
   #Get distances between pairs of animals
   #For each row
   for a1 in animals:
       row = []
       #For each column
       for a2 in animals:
           if a1 == a2:
               row.append('--')
           else:
               distance = a1.distance(a2)
               row.append(str(round(distance, precision)))
       tableVals.append(row)
   #Produce table
   table = pylab.table(rowLabels = rowLabels,
                       colLabels = columnLabels,
                       cellText = tableVals,
                       cellLoc = 'center',
                       loc = 'center',
                       colWidths = [0.15]*len(animals))
   table.scale(1, 1.7)
   table.auto_set_font_size(False)
   table.set_fontsize(10)
   pylab.axis('off')
   pylab.savefig('distances')
   pylab.show()

compareAnimals(animals, 3)

for i in range(len(animals)):
    for j in range(len(animals)):
        if i < j:
            a = animals[i]
            b = animals[j]
            dist = round(a.distance(b), 3)
            print('Distance between', a, 'and', b,
                  'is', dist)

