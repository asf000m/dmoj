# DMOJ ccc18j2
# CCC '18 J2 - Occupy parking

# This is DMOJ problem ccc18j2.

def checkOccupiedParking(spaces, yesterday, today):
    '''
    Check the number of parking spaces that were occupied on two days.
    
    Input:
    - spaces (integer): the total number of parking spaces.
    - yesterday (string): a string wich each character represents the state of
    the parking space of the day before. 'C' indicates occupeid and '.' 
    indicates empty.
    - today (string): a string wich each character represents the state of
    the parking space of the current day. 'C' indicates occupeid and '.' 
    indicates empty.

    Output:
    - integer: the number of occupied parking spaces yesterday and today 
    (both days).

    Ex.:
    >>> checkOccupiedParking(5, 'CC..C', '.CC..')
    1
    >>> checkOccupiedParking(7, 'CCCCCCC', 'C.C.C.C')
    4
    '''

    # loop through each day
    # check if in that day, both spaces were occupied
    # add to a counter if thats true
    # print the value of the counter

    occupied_spaces = 0
    for i in range(spaces):
        state_yesterday = yesterday[i]
        state_today = today[i]
        if state_yesterday == state_today == 'C':
            occupied_spaces += 1
    
    return occupied_spaces

spaces = int(input())
yesterday = input()
today = input()
print(checkOccupiedParking(spaces, yesterday, today))

# print(checkOccupiedParking(5, 'CC..C', '.CC..'))
# print(checkOccupiedParking(7, 'CCCCCCC', 'C.C.C.C'))