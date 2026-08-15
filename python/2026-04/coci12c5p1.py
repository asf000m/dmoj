# DMOJ coci12c5p1
# COCI '12 Contest 5 #1 Ljestvica

composition = input().split('|')

minor_count = 0
major_count = 0

for tone in composition:
    if tone[0] in 'ADE':
        minor_count += 1
    if tone[0] in 'CFG':
        major_count += 1

if minor_count == major_count:
    if tone[-1] in 'ADE':
        minor_count += 1
    if tone[-1] in 'CFG':
        major_count += 1

if minor_count > major_count:
    print('A-mol')
else:
    print('C-dur')
