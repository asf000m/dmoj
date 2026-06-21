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

        sales_in_day = [int(sales) for sales in user_input]
        
        # sum all the sales from the franchises in the day
        sum_sales_in_day = sum(sales_in_day)
        # check if the sum of the sales is a multiple of 13
        if sum_sales_in_day / 13 - int(sum_sales_in_day / 13) == 0:
            multiples_13 += int(sum_sales_in_day / 13)
        
        goods_sold.append(sales_in_day)

    sums_sales_franchise = []
    i = 0
    while i < franchises:
        sales_franchise = 0
        
        # sum the sales of all days of a franchise
        for sales_in_day in goods_sold:
            sales_franchise += sales_in_day[i]
        
        sums_sales_franchise.append(sales_franchise)

        i += 1

    for sum_franchise in sums_sales_franchise:
        if sum_franchise / 13 - int(sum_franchise / 13) == 0:
            multiples_13 += int(sum_franchise / 13)
    
    outputs_multiples_13.append(multiples_13)

for output in outputs_multiples_13:
    print(output)
