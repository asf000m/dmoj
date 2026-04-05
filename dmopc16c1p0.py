# DMOJ dmopc16c1p0
# DMOPC '16 Contest 1 P0 - C.C. and Cheese-kun

width = int(input())
cheese_percent = int(input())

if width == 3 and cheese_percent >= 95:
    satisfaction = 'absolutely'
elif width == 1 and cheese_percent <= 50:
    satisfaction = 'fairly'
else:
    satisfaction = 'very'

print(f'C.C. is {satisfaction} satisfied with her pizza.')
