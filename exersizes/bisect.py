#import pudb; pu.db

filepath = "../code/words.txt"

def in_bisect(space, target, leftindex = 0, rightindex=-1):
    if space == []:
        return None
    if rightindex == -1:
        rightindex = len(space)-1
    elif leftindex == rightindex:
        if space[0] == target:
            return leftindex
        else:
            return None
    midindex = len(space) // 2 # Rounded down.
    leftside = space[:midindex] # Not including midindex
    rightside = space[midindex:] # including midindex
    if target < space[midindex]:
        return in_bisect(leftside, target, leftindex, leftindex+len(leftside)-1)
    else:
        return in_bisect(rightside, target, rightindex-len(rightside)+1, rightindex)


def is_reverse_pair(alphaword, betaword):
    alphalen = len(alphaword)
    betalen = len(betaword)
    if alphalen != betalen:
        return False
    for i in range(alphalen):
        if alphaword[i] != betaword[-(i+1)]:
            return False
    return True

def unzip(word):
    warp = word[0::2]
    weft = word[1::2]
    return (warp, weft)

def trizip(word):
    warp = word[0::3]
    weft = word[1::3]
    worl = word[2::3]
    return (warp, weft, worl)



if __name__=="__main__":
    fullt = []
    for i in range(40):
        fullt.append([])
    with open(filepath) as wrdfile:
        for line in wrdfile:
            stripped = line.strip()
            length = len(stripped)
            fullt[length].append(stripped)
    print(unzip('schooled'))
#   for group in fullt:
#       for word in group:
#           revword = word[::-1]
#           if(in_bisect(group, revword) is not None):
#               print(word,revword)
    for group in fullt:
        for word in group:
            treble = trizip(word)
            warp = treble[0]
            weft = treble[1]
            worl = treble[2] 
            warplen = len(warp)
            weftlen = len(weft)
            worllen = len(worl)
            warpspace = fullt[warplen]
            weftspace = fullt[weftlen]
            worlspace = fullt[worllen]
            if ((in_bisect(warpspace, warp) is not None) and
                (in_bisect(weftspace, weft) is not None) and
                (in_bisect(worlspace, worl) is not None)):
                print(warp, end=' ')
                print(weft, end=' ')
                print(worl, end=' ')
                print(word, end='\n')
