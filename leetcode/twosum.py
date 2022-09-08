"""class twosum(object):
    def __init__(self):
        self.result = bool"""

def twoSumNaive(num_arr, pair_sum):
 
    # search first element in the array
    # First loop -- O(n)
        for i in range(len(num_arr)-1):
            # search other element in the array
            # Second loop -- O(n)
            for j in range( i+1,len(num_arr)):
            # if these two elemets sum to pair_sum, print the pair 
                target = pair_sum == num_arr[i] + num_arr[j]                   
                if target:
                    #return num_arr, pair_sum
                    print("Pair with sum", pair_sum,"is: (", num_arr[i],",",num_arr[j],")")
            #Total - O(n**2)
                    
                    
            """if num_arr[i] + num_arr[j] != pair_sum:
                    print("Not found!")"""
            #Leetcode Version
            """for i in range(len(nums)-1):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j] == target:
                        #result = nums.index(i,j)
                        return i,j"""
                    
            
            #Correct version
            """if num_arr[i] + num_arr[j] == pair_sum:
                    print("Pair with sum", pair_sum,"is: (", num_arr[i],",",num_arr[j],")")
                elif num_arr[i] + num_arr[j] != pair_sum:
                    print("Not found!")"""
                
            """"elif num_arr[i] + num_arr[j] != pair_sum:
                    return "Not found!"""""
                
            """elif pair_sum != True:
                    return "Not found!"   """ 
    #def verify(num_arr,pair_sum):
        

      

# Driver Code
num_arr = [3, 5, 2, -4, 8, 11]
pair_sum = 7
#empty_sum = 9

# Function call inside print
twoSumNaive(num_arr, pair_sum) 

