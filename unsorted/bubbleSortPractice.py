li = [9,1,3,7,5,1,2,4,7,6,2,0]

i = 0

while i < len(li):
    go = 0
    while go < len(li) - i - 1:
        if li[go+1] < li[go]:
            swap = li[go+1]
            li[go+1] = li[go]
            li[go] = swap
        go = go + 1
    i = i + 1
print(li)


list1 = [3,6,8,1,3,2,6,6,10,12,20,13,17]
index = 0

while index < len(list1):
    j = 0
    while j < len(list1) - index - 1:
        if list1[j+1] < list1[j]:
            swap = list1[j+1]
            list1[j+1] = list1[j]
            list1[j] = swap
        j = j + 1
    index = index + 1
print(list1)

newlist = [12,45,76,92,37,0]

anotherIndex = 0

while anotherIndex < len(newlist):
    tempy = 0
    while tempy < len(newlist) - anotherIndex - 1:
        if newlist[tempy+1] < newlist[tempy]:
            swap = newlist[tempy+1]
            newlist[tempy+1] = newlist[tempy] 
            newlist[tempy] = swap
        tempy = tempy + 1
    anotherIndex = anotherIndex + 1
print(newlist)
        
        