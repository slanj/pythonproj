def count7(N, count = 0):
    '''
    N: a non-negative integer
    '''
    # Your code here

    if N < 7:
        return count
    elif N % 10 == 7:
        return count7(N // 10, count + 1)
    else:
        return count7(N // 10, count)



print(count7(77))
