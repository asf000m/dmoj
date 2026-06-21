# DMOJ ecoo17r3p1
# ECOO '17 R3 P1 - Baker Brie


datasets = 10
outputs_multiples_13 = []

for _ in range(datasets):

    # INPUT: F and D
    user_input = input().strip().split()

    # F
    franchises = int(user_input[0])
    # D
    days = int(user_input[1])

    goods_sold = []
    multiples_13 = 0
    for _ in range(days):
        # baked goods sold in a day in each franchise
        user_input = input().strip().split()

        sells_in_day = [int(sells) for sells in user_input]
        
        # sum all the sells from the franchises in the day
        sum_sells_in_day = sum(sells_in_day)
        # check if the sum of the sells is a multiple of 13
        if sum_sells_in_day / 13 - int(sum_sells_in_day / 13) == 0:
            multiples_13 += int(sum_sells_in_day / 13)
        
        goods_sold.append(sells_in_day)

    sums_sells_franchise = []
    i = 0
    while i < franchises:
        sells_franchise = 0
        
        # sum the sells of all days of a franchise
        for sells_in_day in goods_sold:
            sells_franchise += sells_in_day[i]
        
        sums_sells_franchise.append(sells_franchise)

        i += 1

    for sum_franchise in sums_sells_franchise:
        if sum_franchise / 13 - int(sum_franchise / 13) == 0:
            multiples_13 += int(sum_franchise / 13)
    
    outputs_multiples_13.append(multiples_13)

for output in outputs_multiples_13:
    print(output)
