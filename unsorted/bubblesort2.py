list1 = [201,45,7,90,104]
i = 0

while i < len(list1):
    temp = 0
    while temp < len(list1) - i - 1:
        if list1[temp+1] < list1[temp]:
            swap = list1[temp+1]
            list1[temp+1] = list1[temp]
            list1[temp] = swap
        temp = temp + 1
    i = i + 1

"""
for i in len(list1):
    #temp = 0
    for temp in list1 - i - 1:
        if list1[temp+1] < list1[temp]:
            swap = list1[temp+1]
            list1[temp+1] = list1[temp]
            list1[temp] = swap
"""

print(list1)