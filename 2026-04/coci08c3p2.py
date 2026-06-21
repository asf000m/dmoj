# DMOJ coci08c3p2
# COCI '08 Contest 3 #2 Kemija


VOWELS = 'aeiouAEIOU'

secret = input()
original = ''

i = 0
while i <= len(secret) - 1:
    ch = secret[i]
    # check if current character is a vowel and if the next ones are 'p' and the vowel; if True, skip them
    if ch in VOWELS and secret[i + 1] == 'p' and secret[i + 2] == ch:
        original += ch
        i += 3
    else:
        original += ch
        i += 1

print(original)