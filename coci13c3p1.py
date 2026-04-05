# DMOJ coci13c3p1
# COCI '13 Contest 3 #1 Riječi

presses = int(input())

if presses > 1:
    state_1 = 0
    state_2 = 1
    for _ in range(presses - 1):
        state_3 = state_2 + state_1
        state_1 = state_2
        state_2 = state_3

    a_count = state_1
    b_count = state_2

    print(f'{a_count} {b_count}')
else:
    print('0 1')