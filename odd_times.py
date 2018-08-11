def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    odd = 0
    nums = {}
    odd_times = {}
    for num in L:
        nums[num] = nums.get(num, 0) + 1

    for key, num in nums.items():
        if num % 2 != 0:
            odd_times[key] = num

    for num in odd_times.keys():
        if num > odd:
            odd = num

    if odd == 0:
        return None

    return odd

print(largest_odd_times([6, 8, 6, 8, 6, 8, 6, 8, 6, 8]))
