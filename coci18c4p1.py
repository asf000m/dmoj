# DMOJ coci18c4p1
# COCI '18 Contest 4 #1 Elder

current_wizard = input()
number_duels = int(input())
previous_owner = ''

diff_wizards = 1
for _ in range(number_duels):
    duel = input().split()
    winner = duel[0]
    loser = duel[1]
    if current_wizard == loser:
        if not winner in previous_owner:
            diff_wizards += 1
        previous_owner += current_wizard
        current_wizard = winner

print(current_wizard)
print(diff_wizards)
