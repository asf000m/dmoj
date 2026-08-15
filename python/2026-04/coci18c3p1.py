# DMOJ coci18c3p1
# COCI '18 Contest 3 #1 Magnus


def checkHONI(string):
    '''
    Verify if there is enough letters to make the substring HONI, and output
    the number of substrings possible.
    '''

    substrings = []
    substr = ''
    for char in string:
        if char == 'H' and not 'H' in substr:
            substr += char
        elif char == 'O' and not 'O' in substr and 'H' in substr:
            substr += char
        elif char == 'N' and not 'N' in substr and 'HO' in substr:
            substr += char
        elif char == 'I' and not 'I' in substr and 'HON' in substr:
            substr += char
        else:
            continue

        if len(substr) == 4:
            substrings.append(substr)
            substr = ''
    
    # print(substrings)
    print(len(substrings))

string = input()
checkHONI(string)

# checkHONI('MAGNUS')
# checkHONI('HHHHOOOONNNNIIII')
# checkHONI('PROHODNIHODNIK')