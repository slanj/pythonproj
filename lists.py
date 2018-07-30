# Lists are mutable
l = []
li = [5, 3, 5, "words"]
li[3] = "more words"
print(li[3])

# Elements are accessed by index
i = 4
li[i-1] = li[i-1] + ", less words"
print(li[i-1])

# You can iterate over a list
total = 0
nums = [4, 5, 6, 7, 1]

for i in nums:
    total += i

print(total)

# If you copy a list - you create a new name for a same object (aliasing)
first_list = [22, 33, 44]
second_list = first_list
second_list.append(55)
print(first_list)

# Create a new list and copy every element (cloning)
third_list = second_list[:]
second_list.append(66)
print(third_list)

# List operations

# Add elements to the end of the list
nums = [1, 2, 3]
nums.append(4)

# Concatenate
other_nums = [5, 6, 7]
all_nums = nums + other_nums
print(all_nums)

# Extension
all_nums.extend([8, 9, 10])
print(all_nums)

# Delete element at specific index
del(all_nums[0])
print(all_nums)

# Remove element at the end of the list, returns removed element
removed = all_nums.pop()
print(all_nums, removed)

# Remove specific element
all_nums.remove(5)
print(all_nums)

# Convert string to a list
s = "letters"
l = list(s)
print(l)

# Split a string on a character parameter (split on spaces without parameter)
l = s.split('e')
print(l)

# Join list of characters into a string
s2 = 'e'.join(l)
print(s2)

# sorted - returns a new sorted list
sorted_list = sorted(l)
print(sorted_list)

# sort - mutates existing list
more_nums = [3, 1, 7, 7, 3, 2]
more_nums.sort()
print(more_nums)

# reverse - mutates existing list
more_nums.reverse()
print(more_nums)