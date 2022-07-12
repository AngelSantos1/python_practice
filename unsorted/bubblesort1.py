list1 = [212,12,42,6,90,0]
i = 0
#temp = 0

while i < len(list1):
    temp = 0
    while temp < len(list1) - i - 1:        
        if list1[temp+1] > list1[temp]:
            swap = list1[temp+1]
            list1[temp+1] = list1[temp]
            list1[temp] = swap
        temp = temp + 1
    i = i + 1

print(list1)