# DMOJ ccc00s1
# CCC '00 S1 - Slot Machines

# This is DMOJ problem ccc00s1.

quarters = int(input())
first_machine = int(input())
second_machine = int(input())
third_machine = int(input())

next_play = 1

plays = 0

while quarters > 0:
    if next_play == 1:
        next_play = 2
        plays += 1
        quarters -= 1
        first_machine += 1
        
        if first_machine == 35:
            first_machine = 0
            quarters += 30
    
    elif  next_play == 2:
        next_play = 3
        plays += 1
        quarters -= 1
        second_machine += 1
        
        if second_machine == 100:
            second_machine = 0
            quarters += 60
    
    elif next_play ==  3:
        next_play = 1
        plays += 1
        quarters -= 1
        third_machine += 1
        
        if third_machine == 10:
            third_machine = 0
            quarters += 9
    
print(f'Martha plays {plays} times before going broke.')