# DMOJ ccc18j1
# CCC '18 J1 - Telemarketer or not?

digit_1 = int(input())
digit_2 = int(input())
digit_3 = int(input())
digit_4 = int(input())

if (digit_1 in (8, 9) and digit_4 in (8, 9)) and digit_2 == digit_3:
    print('ignore')
else:
    print('answer')
