# DMOJ ccc15j1
# CCC '15 J1 - Special Day

month = int(input())
day = int(input())
date = f'2015-{month}-{day}'

if date < '2015-2-18':
    print('Before')
elif date > '2015-2-18':
    print('After')
else:
    print('Special')
