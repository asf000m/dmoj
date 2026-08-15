# This is DMOJ problem ecoo17r1p1.


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
    
    idx_highest = year_students.index(max(year_students))
    year_students[idx_highest] += diff_total_students
    
    proceeds = 0
    for i in range(len(year_students)):
        proceeds += year_students[i] * YEAR_COSTS[i]
    
    if proceeds / 2 >= trip_cost:
        outputs.append('NO')
    else:
        outputs.append('YES')

# OUTPUT
for output in outputs:
    print(output.strip())
