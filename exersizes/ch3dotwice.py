def dotwice(f,n):
    f(n)
    f(n)

def print_spam():
    print('spam')

dotwice(print_spam)
