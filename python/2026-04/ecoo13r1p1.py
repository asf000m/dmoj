# DMOJ ecoo13r1p1
# ECOO '13 R1 P1 - Take a Number


students_late = 0  # number of students who were late that day
students_remained = 0  # number of students who remained in line after the desk was closed

# inputs
next_number = int(input())  # next number in the take a number machine

activity = ''
while activity != 'EOF':
    activity = input()  # represent the activity at the attendance desk
    
    if activity == 'TAKE':  # a student has arrived and taken the next number
        students_late += 1
        students_remained += 1
        if next_number == 999:
            next_number = 1
        else:
            next_number += 1
    elif activity == 'SERVE':  # the attendance secretary has served the next student in line
        students_remained -= 1
    elif activity == 'CLOSE':  # the desk has closed for the day
        print(students_late, students_remained, next_number)
        students_late = 0
        students_remained = 0
