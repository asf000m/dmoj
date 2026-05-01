# DMOJ ecoo17r1p1
# ECOO '17 R1 P1 - Munch 'n' Brunch


test_cases = 10
outputs = []
YEAR_COSTS = [12, 10, 7, 5]

for _ in range(test_cases):
    # INPUT
    trip_cost = int(input())
    proportions = input().split(' ')
    total_students = int(input())

    # SOLUTION
    year_students = []
    for proportion in proportions:
        year_students.append(int(float(proportion) * total_students))

    diff_total_students = abs(total_students - sum(year_students))
    
    proceeds = 0
    for i in range(len(year_students)):
        proceeds += year_students[i] * YEAR_COSTS[i]

    highest_attendees = sorted(year_students)[-1]
    for i in range(len(year_students)):
        if highest_attendees == year_students[i]:
            proceeds += diff_total_students * YEAR_COSTS[i]
    
    if proceeds / 2 >= trip_cost:
        outputs.append('NO')
    else:
        outputs.append('YES')

# OUTPUT
for output in outputs:
    print(output.strip())
