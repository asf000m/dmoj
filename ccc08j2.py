# DMOJ ccc08j2
# CCC '08 J2 - Do the Shuffle


playlist = 'ABCDE'

while True:
    button = int(input())
    times = int(input())

    if button == 1:
        for _ in range(times):
            playlist = playlist[1:] + playlist[0]
    elif button == 2:
        for _ in range(times):
            playlist = playlist[-1] + playlist[:-1]
    elif button == 3:
        for _ in range(times):
            playlist = playlist[1] + playlist[0] + playlist[2:]
    elif button == 4:
        break

output = ''
for song in playlist:
    output += song + ' '
output = output.strip()
print(output)