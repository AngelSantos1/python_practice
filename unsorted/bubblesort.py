#begin at index 0
indexPointer = 0

#the list to be sorted
listToSort = ['a','e','d','c'] 

#keep iterating while less than the List size
while indexPointer < len(listToSort):
    #new variable 
    go = 0
    while go < len(listToSort) - indexPointer - 1:
        #- indexPointer - 1 - do not check last number in list
        
        if listToSort[go+1] < listToSort[go]:
            
            swap = listToSort[go+1]
            
            #swap = listToSort[go]
            # results in ['a', 'e', 'e', 'e']            
            
            listToSort[go+1] = listToSort[go]
            
            #listToSort[go] = listToSort[go]
            #results in ['a', 'c', 'c', 'c']
            
            
            
            listToSort[go] = swap
        go = go + 1
    indexPointer = indexPointer + 1
print(listToSort)