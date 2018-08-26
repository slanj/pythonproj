class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <joy:' + str(self.value) + ', calories:' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    """
    names, values, calories are lists of same length.
    name is a list of strings
    values and calories are lists of numbers
    returns list of Foods
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu

def greedy(items, maxCost, keyFunction):
    '''
    Assumes items a list, maxCost >= 0,
    kyFunction maps elements of items to numbers
    '''
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print('     ', item)

def testGreedys(maxUnits):
    print("Use greedy by joy to allocate ", maxUnits, ' calories')
    testGreedy(mymenu, maxUnits, Food.getValue)

    print('\nUse greedy by calories to allocate ', maxUnits, ' calories')
    testGreedy(mymenu, maxUnits, lambda x: 1/Food.getCost(x))

    print('\nUse greedy by density to allocate ', maxUnits, ' calories')
    testGreedy(mymenu, maxUnits, Food.density)


mymenu = buildMenu(['apple', 'burger', 'potato', 'carrot'], [42, 39, 2, 15], [88, 100500, 15, 8])

for item in mymenu:
    print(item)

testGreedys(90)




