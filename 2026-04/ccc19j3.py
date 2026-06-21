# DMOJ ccc19j3
# CCC '19 J3 - Cold Compress


output = ''

# input
lines = int(input())  # number of lines

for _ in range(lines):
    line = input()  # line of input characters
    
    counted_line = ''
    current_ch = ''
    
    i = 0
    while i < len(line):
        ch = line[i]
    
        if ch not in current_ch:  # if ch was not counted yet
            if current_ch:
                counted_line += f'{len(current_ch)} {current_ch[0]} '
                current_ch = ''
    
        current_ch += ch
        i += 1

    counted_line += f'{len(current_ch)} {current_ch[0]} '
    
    output += counted_line.strip() + '\n'

# output
print(output.strip())
