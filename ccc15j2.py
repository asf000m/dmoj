# DMOJ ccc15j2
# CCC '15 J2 - Happy or Sad

message = input()

happy_count = message.count(':-)')
sad_count = message.count(':-(')

if happy_count == 0 and sad_count == 0:
    print('none')
elif happy_count > sad_count:
    print('happy')
elif sad_count > happy_count:
    print('sad')
else:
    print('unsure')
