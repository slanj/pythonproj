import re

lines = open('regex_sum_129486.txt')
nums = []

for line in lines:
    stuff = re.findall('[0-9]+', line)
    if len(stuff) > 0:
        for s in stuff:
            nums.append(int(s))

print(sum(nums))

# short variant
print( sum( [ int(s) for s in re.findall('[0-9]+', open('regex_sum_129486.txt').read()) ] ) )