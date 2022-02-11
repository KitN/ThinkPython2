import math as m

def mysqrt(a, x, epsilon=0.00000001):
    """ Use guess x to find the square root of a"""
    while True:
        y = (x + a/x)/2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

def printTable(rows=9):
    widths = (4,15,15,15)
    for i, label in enumerate(('a', 'mysqrt(a)', 'math.sqrt(a)', 'diff')):
        print(label, end='')
        print(" "*(widths[i]-len(label)), end='')
    print()
    for w in widths:
        print('-'*(w-1), end='')
        print(' ', end='')
    print()
    for r in range(1, rows+1):
        mine = mysqrt(r,5)
        theirs = m.sqrt(r)
        print(f"{r}", end='')
        print("   ", end='')
        print(f"{mine:.8f}", end='')
        print(' '*5, end='')
        print(f"{theirs:.8f}", end='')
        print(' '*5, end='')
        print(abs(mine-theirs))


print(mysqrt(2, 1.5))
printTable()
