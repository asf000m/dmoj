# DMOJ ccc07j3
# CCC '07 J3 - Deal or No Deal Calculator


cases = [100, 500, 1_000, 5_000, 10_000, 25_000, 50_000, 100_000, 500_000, 1_000_000]

# INPUT
cases_opened = int(input())

opened = []
for _ in range(cases_opened):
    opened.append(int(input()))

offer = int(input())

# SOLUTION
opened.sort()
for case in opened:
    cases[case - 1] = 0

average = sum(cases) / (len(cases) - cases_opened)

response = ''
if average > offer:
    response = 'no deal'
else:
    response = 'deal'

# OUTPUT
print(response)
