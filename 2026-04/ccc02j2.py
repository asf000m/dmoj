# DMOJ ccc02j2
# CCC '02 J2 - AmeriCanadian


VOWELS = 'aeiouAEIOU'
word = ''
words = ''

while word != 'quit!':
    word = input()
    idx = word.rfind('or')
    if word.endswith('or') and word[idx - 1] not in VOWELS:
        words += word[:idx] + 'our' + ' '
    else:
        words += word + ' '

for word in words.strip().split():
    if word != 'quit!':
        print(word)