###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


def sort_dic(dic):
    '''Assumes dic is dictionary (key:value).
    Returns dic sorted by value'''
    ord_dic = {}
    for value in sorted(dic.values(), reverse = True):
        for key in dic:
            if dic[key] == value:
                ord_dic[key] = value
    return ord_dic


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    ships = []
    container = []
    ship_weight = 0

    sorted_cows = sorted([[value, key] for (key,value) in cows.items()], reverse = True)

    while len(sorted_cows) > 0:
        last_cows = []
        for c in sorted_cows:
            if ship_weight + c[0] <= limit:
                container.append(c[1])
                ship_weight += c[0]
            else:
                last_cows.append(c)
        ships.append(container)
        container = []
        ship_weight = 0
        sorted_cows = last_cows

    return ships



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    ship_weights = []
    for combinations in sorted((get_partitions(cows.keys())), key=lambda x: len(x)):
        for c in combinations:
            ship_weights.append(sum([cows[i] for i in c]))
        vzletit = True
        for w in ship_weights:
            if w > limit:
                vzletit = False
                break
        ship_weights = []
        if vzletit:
            return combinations



# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')

    start = time.time()
    print(greedy_cow_transport(cows, 10))
    end = time.time()
    print(end - start)

    start = time.time()
    print(brute_force_cow_transport(cows, 10))
    end = time.time()
    print(end - start)




"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""


compare_cow_transport_algorithms()


cows = load_cows('ps1_cow_data.txt')
print(sort_dic(cows))

'''
{'Betsy': 9, 'Henrietta': 9, 'Herman': 7, 'Oreo': 6, 'Millie': 5, 'Maggie': 3, 'Moo Moo': 3, 'Milkshake': 2, 'Lola': 2, 'Florence': 2}
'''

