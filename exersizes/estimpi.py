import math

frontconstant = 2*math.sqrt(2)/9801
EPSILON = 1e-15

def bang(n):
    return math.factorial(n)

def termk(k):
    numerator = bang(4*k)*(1103 + 26390*k)
    denominator = bang(k)**4 * 396**(4*k)
    return numerator/denominator


def estimate(epsilon):
    k = 0
    term = 1
    total = 0
    while term > epsilon:
        term = termk(k)
        total += term
        print(f"Total is now {total}")
        k += 1
    return frontconstant*total

print(estimate(EPSILON))
print(1/math.pi)
