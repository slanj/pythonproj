def printMove(fr, to):
    print('move from', str(fr), 'to', str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        print('First call in', str(n), 'scope')
        Towers(n - 1, fr, spare, to)

        print('Next call in', str(n), 'scope')
        Towers(1, fr, to, spare)

        print('Final call in', str(n), 'scope')
        Towers(n - 1, spare, to, fr)

        print('Done with', str(n), 'scope')

Towers(3, "P1", "P2", "P3")

