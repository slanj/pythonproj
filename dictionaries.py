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
