def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    num = int(us_num)

    if num < 11:
        mandarin = trans[us_num]
    elif num < 20:
        mandarin = trans['10'] + " " + trans[str(num % 10)]
    elif num % 10 == 0:
        mandarin = trans[str(num // 10)] + " " + trans['10']
    else:
        mandarin = trans[str(num // 10)] + " " + trans['10'] + " " + trans[str(num % 10)]

    return mandarin

print(convert_to_mandarin("36"))
