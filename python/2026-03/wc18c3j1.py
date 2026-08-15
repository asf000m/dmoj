# DMOJ wc18c3j1

p = int(input())
b = int(input())
d = int(input())

painted_badges = p // b
leftover_paint = p - (painted_badges * b)

pokedollars = (painted_badges * d) + leftover_paint

print(pokedollars)
