# Tuples sre immutable
te = (2, "some", 42)
answer = te[2]

#slice tuple
some_answer = te[1:3]
print(te, answer, some_answer)

# Concatenate tuples
ste = te + (5, 55)
print(ste)

x = 3
y = 73

# Using tuple for swaping variables
(x, y) =  (y, x)
print(x, y)

# Using tuple to return more than one value from a function
def qq(x, y):
    q = x // y
    r = x % y
    return (q, r)

(x, y) = qq(x, y)
print(x, y)

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        #it is important to add a comma for program to understand that it is tuple with single element
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)

(small, large, words) =  get_data(((1, "mine"),
                                   (3, "yours"),
                                   (5, "ours"),
                                   (7, "mine")))

print (small, large, words)