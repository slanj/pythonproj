def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif aStr == char:
        return True
    elif len(aStr) == 1:
        return False
    else:
        mid = int(len(aStr) / 2)
        if aStr[mid] > char:
            return isIn(char, aStr[0:mid])
        else:
            return isIn(char, aStr[mid:len(aStr)])
