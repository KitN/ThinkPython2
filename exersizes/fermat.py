# Fermat Checker
def check_fermat(a,b,c,n):
    lhs = a**n + b**n
    rhs = c**n
    if lhs == rhs:
        print('Holy Smokes')
    else:
        print('No, that doesn work')


check_fermat(1,2,3,3)

constants = []
for letter in ['a', 'b', 'c', 'n']:
    prompt = "Enter value for {} ".format(letter) 
    constants.append(input(prompt))


a, b, c , n = int(constants[0]), int(constants[1]), int(constants[2]), int(constants[3])
check_fermat(a,b,c,n)
