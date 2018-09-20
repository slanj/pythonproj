#!/bin/python3

import os
import sys

#
# Complete the kingRichardKnights function below.
#
def kingRichardKnightsSlow(n, s, knights, find):
    coords = []
    for f in find:
        nashel = False
        while not nashel:
            for i in range(len(knights)):
                for j in range(len(knights)):
                    if knights[i][j] == f:
                        coords.append((i+1, j+1))
                        nashel = True
    return coords

def kingRichardKnights():
    res = []
    for f in find:
        res.append(coords[f])
    return res


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    kfile = open("knights.txt")

    # INPUT FIRST VARS
    #n = int(input())
    #s = int(input())

    n = int(kfile.readline())
    s = int(kfile.readline())

    knights = []

    for i in range(n):
        knights.append([(i*n)+h for h in range(n)])

    commands = []
    for turn in range(s):
        commands.append(list(map(int, kfile.readline().rstrip().split())))
    # INPUT COMMANDS
    #for _ in range(s):
    #    commands.append(list(map(int, input().rstrip().split())))

    coords = {}
    for i in range(n):
        for j in range(n):
            coords[knights[i][j]] = (i+1, j+1)

    for command in commands:
        a = command[0]-1
        b = command[1]-1
        d = command[2]+1
        temp = []
        for i in range(a, a+d):
            temp.append([knights[i][j] for j in range(b,b+d)])

        transformed = []
        for h in range(len(temp)):
            transformed.append([temp[l][h] for l in range(len(temp)-1, -1, -1)])

        for i in range(a, a+d):
            for j in range(b, b+d):
                knights[i][j] = transformed[i-a][j-b]
                coords[knights[i][j]] = (i+1, j+1)

    #k = int(input())
    k = int(kfile.readline())
    find = []
    for turn in range(k):
        find.append(int(kfile.readline().rstrip()))
    #for turn in range(k):
    #    find.append(int(input().rstrip()))



    result = kingRichardKnights()


    # PRINT RESULTS
    print('\n'.join([' '.join(map(str, x)) for x in result]))
    #print(coords)
    #fptr.close()