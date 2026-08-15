# DMOJ ccc06j1
# CCC '06 J1 - Canadian Calorie Counting


# calories of burgers
CHEESEBURGER = 461
FISH_BURGER = 431
VEGGIE_BURGER = 420

# calories of sides
FRIES = 100
BAKED_POTATO = 57
CHEF_SALAD = 70

# calories of drinks
SOFT_DRINK = 130
ORANGE_JUICE = 160
MILK = 118

# calories of desserts
APPLE_PIE = 167
SUNDAE = 266
FRUIT_CUP = 75

# choices of burger, side, drink and dessert
burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

total_calories = 0

if burger == 1:
    total_calories += CHEESEBURGER
elif burger == 2:
    total_calories += FISH_BURGER
elif burger == 3:
    total_calories += VEGGIE_BURGER

if side == 1:
    total_calories += FRIES
elif side == 2:
    total_calories += BAKED_POTATO
elif side == 3:
    total_calories += CHEF_SALAD

if drink == 1:
    total_calories += SOFT_DRINK
elif drink == 2:
    total_calories += ORANGE_JUICE
elif drink == 3:
    total_calories += MILK

if dessert == 1:
    total_calories += APPLE_PIE
elif dessert == 2:
    total_calories += SUNDAE
elif dessert == 3:
    total_calories += FRUIT_CUP

print(f'Your total Calorie count is {total_calories}.')
