# DMOJ ccc11s2
# CCC '11 S2 - Multiple Choice

'''
Input:
- choices (integer): number of N answer choices for the questions.
- answers (list): list with 2N items composed of N student responses followed by
N correct answers for the N choices.

Output:
- integer: number of questions the student answered correctly.

Examples:
>>> 3
>>> A
>>> B
>>> C
>>> A
>>> C
>>> B
1
'''

choices = int(input())

responses = []
for _ in range(choices):
    response = input()
    responses.append(response)

correct_answers = []
for _ in range(choices):
    answer = input()
    correct_answers.append(answer)

correct_responses = 0
for response, answer in zip(responses, correct_answers):
    if response == answer:
        correct_responses += 1

print(correct_responses)