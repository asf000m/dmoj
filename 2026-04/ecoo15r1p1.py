# DMOJ ecoo15r1p1
# ECOO '15 R1 P1 - When You Eat Your Smarties


output = ''
test_cases = 10

i = 0
while i < test_cases:
    orange = 0
    blue = 0
    green = 0
    yellow = 0
    pink = 0
    violet = 0
    brown = 0
    red = 0

    # input
    color = ''
    while color != 'end of box':
        color = input()  # holds the color of a single Smartie

        if color == 'orange':
            orange += 1
        elif color == 'blue':
            blue += 1
        elif color == 'green':
            green += 1
        elif color == 'yellow':
            yellow += 1
        elif color == 'pink':
            pink += 1
        elif color == 'violet':
            violet += 1
        elif color == 'brown':
            brown += 1
        elif color == 'red':
            red += 1

    seconds = (orange // 7) * 13
    if orange % 7 != 0:
        seconds += 13

    seconds += ((blue // 7) * 13)
    if blue % 7 != 0:
        seconds += 13

    seconds += (green // 7) * 13
    if green % 7 != 0:
        seconds += 13

    seconds += (yellow // 7) * 13
    if yellow % 7 != 0:
        seconds += 13

    seconds += (pink // 7) * 13
    if pink % 7 != 0:
        seconds += 13

    seconds += (violet // 7) * 13
    if violet % 7 != 0:
        seconds += 13

    seconds += (brown // 7) * 13
    if brown % 7 != 0:
        seconds += 13

    seconds += red * 16

    output += f'{seconds}\n'

    i += 1

# output
print(output.strip())
