# DMOJ wc17c3j3
# WC '17 Contest 3 J3 - Uncrackable


def checkPassword(password):
    ''' 
    Receive a string and check if is a valid password with the following conditions:
        - have 8 to 12 characters long (inclusive);
        - every character is either a lowercase letter (a...z), uppercase letter
        (A...Z), or digit (0...9);
        - it must contain at least three lowercase letters, at least two uppercase
        letters, and at least one digit.
    '''
    LOWERCASE = 3
    UPPERCASE = 2
    DIGIT = 1
    OTHER = 0

    lowercases = 0
    uppercases = 0
    digits = 0
    others = 0

    if 8 <= len(password) <= 12:
        for char in password:
            if char.islower():
                lowercases += 1
            elif char.isupper():
                uppercases += 1
            elif char.isdigit():
                digits += 1
            else:
                others += 1
        
        if lowercases >= LOWERCASE and uppercases >= UPPERCASE and digits >= DIGIT and others == OTHER:
            validity = 'Valid'
        else:
            validity = 'Invalid'
    else:
        validity = 'Invalid'
    
    # print(
    #     f'Result:\t\t{validity}\n'
    #     f'Input:\t\t{password}\n'
    #     f'Length:\t\t{len(password)}\n'
    #     f'Lowercases:\t{lowercases}\n'
    #     f'Uppercases:\t{uppercases}\n'
    #     f'Digits:\t\t{digits}\n'
    #     f'Others:\t\t{others}\n'
    # )
    
    return validity

# password1 = 'PassW0rd'
# password2 = 'CorrectHorseBatteryStaple'
# checkPassword(password1)
# checkPassword(password2)

password = input()
print(checkPassword(password))
