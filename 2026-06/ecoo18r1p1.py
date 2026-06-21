# DMOJ ecoo18r1p1
# ECOO '18 R1 P1 - Willow's Wild Ride


dataset_results = []
datasets = 10

for _ in range(datasets):
    # INPUT
    user_input = input().split(' ')

    # days that Willow plays with a box before getting bored of it
    plays = int(user_input[0])  
    
    # days that Mandy comes home
    days = int(user_input[1])  
    
    # represent whether Mandy came home empty-handed ('E') or with a box ('B')
    box_per_day = []
    for i in range(days):
        box_per_day.append(input())
    
    plays_left = 0

    for box in box_per_day:
        if box == "B":
            plays_left += plays
        
        if plays_left > 0:
                plays_left -= 1
    
    dataset_results.append(plays_left)

# OUTPUT
for result in dataset_results:
    print(result)

