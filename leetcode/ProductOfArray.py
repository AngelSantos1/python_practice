def ProductOfArray(array):
    result = [1] * (len(array))
    prefix = 1 
    
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= array[i]
    
    
    answer = []
    for i in range(len(array)-1):
        product = array[i] * array[i+1] 
        answer.append(product)
        #for j in range(i + 1, len(array)):
            #if array[i] != array[i]:
            #answer.append(array[i+1] * array[j])
    return answer



array = [1,2,3,4]
# Output [24, 12, 8, 6]

print(ProductOfArray(array))