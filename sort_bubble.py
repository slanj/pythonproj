def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j], L[j-1] = L[j-1], L[j]

L = [34, 555, 33, 32, 32, 46, 1, 23, 4344]
bubble_sort(L)
print(L)