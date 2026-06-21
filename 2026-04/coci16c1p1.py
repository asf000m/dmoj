# DMOJ coci16c1p1
# COCI '16 Contest 1 #1 Tarifa

def megabytesAvailable(megabytes, months, usages):
    '''
    Calculate the number of megabytes available for the next month.
    
    Input:
    - megabytes (integer): number of megabytes given per month.
    - months (integer): number of months.
    - usages (list): list of integer that represents the number of megabytes
    used in each month.
    
    Output:
    - integer: number of megabytes available for the next month.

    Example:
    >>> megabytesAvailable(10, 12, [5, 6, 7, 3, 1, 3, 4, 8, 9, 10, 3, 4])
    67
    >>> megabytesAvailable(10, 3, [4, 6, 2])
    28
    '''
    next = 0
    for i in range(months):
        # print(f'{next} + {megabytes} - {usages[i]}')
        next = next + megabytes - usages[i]
    
    return next + megabytes

# tests
# print(megabytesAvailable(10, 12, [5, 6, 7, 3, 1, 3, 4, 8, 9, 10, 3, 4]))
# print(megabytesAvailable(10, 3, [4, 6, 2]))

megabytes = int(input())
months = int(input())
usages = []
for i in range(months):
    usage = int(input())
    usages.append(usage)

print(megabytesAvailable(megabytes, months, usages))