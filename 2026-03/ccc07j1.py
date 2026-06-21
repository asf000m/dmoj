# DMOJ ccc07j1
# CCC '07 J1 - Who is in the Middle?

weight_1 = int(input())
weight_2 = int(input())
weight_3 = int(input())

if  (weight_2 > weight_1 and weight_1 > weight_3) or (weight_3 > weight_1 and weight_1 > weight_2):
    mama = weight_1
elif (weight_1 > weight_2 and weight_2 > weight_3) or (weight_3 > weight_2 and weight_2 > weight_1):
    mama = weight_2
elif (weight_1 > weight_3 and weight_3 > weight_2) or (weight_2 > weight_3 and weight_3 > weight_1):
    mama = weight_3

print(mama)
