# DMOJ ccc11s1
# CCC '11 S1 - English or French?

def englishOrFrench():
    '''
    Determine if a given text is English or French by counting the number of 
    't' (and 'T') or 's' (and 'S') it has. If there are more t than s in the text, it's 
    probably in English. If there are more s than t, it's probably French. And 
    if their number is equal, it's probably French.

    Input:
    - no input.

    Output:
    - string: The output is the string 'English' or 'French'.

    Example:
    >>> englishOrFrench()
    English
    >>> englishOrFrench()
    French
    '''

    number_t = 0
    number_s = 0

    lines = int(input())
    for _ in range(lines):
        line = input()
        number_t += line.count('t') + line.count('T')
        number_s += line.count('s') + line.count('S')

    if number_t > number_s:
        print('English')
    elif number_s > number_t:
        print('French')
    else:
        print('French')


englishOrFrench()