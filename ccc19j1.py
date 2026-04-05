# This is DMOJ problem ccc19j1.

# scoring for the Apples
apples_3p = int(input())    # 3-point shots
apples_2p = int(input())    # 2-point shots
apples_1p = int(input())    # 1-point shots

# scoring for the Bananas
bananas_3p = int(input())   # 3-point shots
bananas_2p = int(input())    # 2-point shots
bananas_1p = int(input())    # 1-point shots

apples_total = apples_3p * 3 + apples_2p * 2 + apples_1p
bananas_total = bananas_3p * 3 + bananas_2p * 2 + bananas_1p

if apples_total > bananas_total:
    print('A')
elif bananas_total > apples_total:
    print('B')
else:
    print('T')
