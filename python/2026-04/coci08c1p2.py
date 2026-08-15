# DMOJ coci08c1p2
# COCI '08 Contest 1 #2 Ptice


# inputs
questions = int(input())  # number of questions on the exam
correct_answers = input()  # string of N letters A, B and C

# three boys answers
adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'

# problem processing
adrian_correct = 0
bruno_correct = 0
goran_correct = 0

i = 0
while i < questions:
    if correct_answers[i] == adrian[i % len(adrian)]:
        adrian_correct += 1
    if correct_answers[i] == bruno[i % len(bruno)]:
        bruno_correct += 1
    if correct_answers[i] == goran[i % len(goran)]:
        goran_correct += 1
    
    i += 1

largest = adrian_correct
if bruno_correct > largest:
    largest = bruno_correct
elif goran_correct > largest:
    largest = goran_correct

# output
print(largest)

if adrian_correct == largest:
    print('Adrian')
if bruno_correct == largest:
    print('Bruno')
if goran_correct == largest:
    print('Goran')
