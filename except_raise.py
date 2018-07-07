def get_ratios(L1, L2):
    '''
    Assumes: L1 and L2 are lists of equal lengh of numbers
    Returns: a list containing L1[i]/L2[i]
    '''
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))  #Nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

print(get_ratios([1, 2, 3], [1, 0, 3]))