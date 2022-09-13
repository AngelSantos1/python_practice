def twoSumHashing(num_arr, pair_sum):
    # O(n)
    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        #O(log n)
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
        hashTable[num_arr[i]] = num_arr[i]
        
""" def indexHash(num_arr,pair_sum):
    for i in range(num_arr):
        if num_arr[i] in hashTable:
            return [hashTable[num_arr[i]], i]
        #list(iter(hashTable))
        # O(n log n)

#def indexHash(num_arr[], pair_sum[]) """
        
# Driver Code            
hashTable = {}
num_arr = [4, 5, 1, 8, 12]
pair_sum = 9    
  
# Calling function
twoSumHashing(num_arr, pair_sum)
#indexHash(num_arr,pair_sum)

""" 
#print(index(num_arr, pair_sum))
#print(twoSumHashing(num_arr[], pair_sum[])) """

