# Is 'a' a power of 'b'.

def isPowerOf(a,b):
    if a == b:
        return True
    elif a % b == 0:
        return isPowerOf(a/b, b)
    return False


powersof2 = [2**n for n in range(10)]
powersof3 = [3**n for n in range(10)]
powersof4 = [4**n for n in range(10)]
print(powersof2)
print(powersof3)
print(powersof4)

print(isPowerOf(81, 3))
