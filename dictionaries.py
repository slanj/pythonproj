# Dictionary stores pairs of data together - a key and a value

my_dict = {}
grades = {"Ana": 5, "Kolya": 3, "Petya": 4}
num_of_students = len(grades)

# We can add change entries
grades["Misha"] = "B"
grades["Kolya"] = 2

# Test if key in dictionary
an = "Ana" in grades
ko = "Kolya" in grades

# Remove an entry
del(grades["Misha"])

# Get set of keys or values as iterable for loop
grades.keys()
grades.values()

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here

    i = 0
    for value in aDict.values():
        i += len(value)
    return i

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    lens = {}
    for value in aDict:
        lens[value] = (len(aDict[value]))

    m = 0
    i = ""
    for key, value in lens.items():
        if m <= value:
            m = value
            i = key

    print(i)
    return i

biggest(animals)