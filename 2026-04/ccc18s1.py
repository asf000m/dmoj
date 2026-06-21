# DMOJ ccc18s1
# CCC '18 S1 - Voronoi Villages


# input
villages = int(input())

positions = []
for _ in range(villages):
    position = int(input())
    positions.append(position)

# resolution
positions.sort()
sizes = []

# get each position excluding the leftmost and rightmost ones
for i in range(1, villages - 1):
    space_left = (positions[i - 1] + positions[i]) / 2
    space_right = (positions[i + 1] + positions[i]) / 2
    size = space_right - space_left
    sizes.append(size)

# output
smallest = min(sizes)
print(smallest)
