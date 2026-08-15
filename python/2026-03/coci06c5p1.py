# DMOJ coci06c5p1
# COCI '06 Contest 5 #1 Trik

def swapCups(moves):
    moves_list = []
    for move in moves:
        moves_list.append(move)
    
    locations = [1, 0, 0]
    for move in moves_list:
        if move == 'A':
            temp = locations[0]
            locations[0] = locations[1]
            locations[1] = temp
        elif move == 'B':
            temp = locations[1]
            locations[1] = locations[2]
            locations[2] = temp
        elif move == 'C':
            temp = locations[0]
            locations[0] = locations[2]
            locations[2] = temp
        else:
            continue
    
    if locations[0] == 1:
        print(1)
    elif locations[1] == 1:
        print(2)
    elif locations[2] == 1:
        print(3)

moves_string = input()
swapCups(moves_string)
