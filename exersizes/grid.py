bar = " - - - - "
width = len(bar)

def beam():
    beam = '+' + bar + '+' + bar + '+'
    print(beam)

def blank():
    blank = '|' + ' '*width + '|' + ' '*width + '|'
    print(blank)
    print(blank)
    print(blank)
    print(blank)

beam()
blank()
beam()
blank()
beam()
