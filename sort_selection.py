def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

L = [3, 5, 557, 2, 757, 333, 2, 2, 0, 12]
selection_sort(L)
print(L)