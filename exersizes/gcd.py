def gcd(a,b):
    if b == 0:
        return a
    remainder = a % b
    return gcd(b, remainder)

a = 60
b = 120
print(gcd(a,b))
