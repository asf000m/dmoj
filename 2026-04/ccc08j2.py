# DMOJ ccc08j2
# CCC '08 J2 - Do the Shuffle


playlist = 'ABCDE'

while True:
    button = int(input())
    times = int(input())

    if button == 4:
        break
    
    for _ in range(times):
        if button == 1:
            playlist = playlist[1:] + playlist[0]
        elif button == 2:
            playlist = playlist[-1] + playlist[:-1]
        elif button == 3:
            playlist = playlist[1] + playlist[0] + playlist[2:]

output = ''
for song in playlist:
    output += song + ' '
output = output.strip()
print(output)