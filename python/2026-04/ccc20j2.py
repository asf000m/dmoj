# DMOJ ccc20j2
# CCC '20 J2 - Epidemiology


threshold = int(input())
people_with_disease = int(input())
infection_rate = int(input())

total_infected = people_with_disease
days = 0

while total_infected <= threshold:
    days += 1
    total_infected += infection_rate * people_with_disease
    people_with_disease = infection_rate * people_with_disease

print(days)
