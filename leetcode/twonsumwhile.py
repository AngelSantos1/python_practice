nums = [3, 5, 2, -4, 8, 11]
target = 7

i = 0
j = 0

while i < len(nums) - 1:
    #while j < len(nums):        
        #i = i + 1   
        #j = 0
       
    if nums[i] + nums[i+1] == target:
            print(nums[i],nums[i+1]) 
    #j = i + 1  
    i = i + 1


"""while i < len(nums) - 1:
    
    while j < len(nums):        
        #i = i + 1   
        #j = 0
        temp = i + 1    
        if nums[i] + nums[temp] == target:
            print(nums[i],nums[temp])
        j = j + 1    
    i = i + 1
        """
    
        
    

"""nums = [3, 5, 2, -4, 8, 11]
target = 7

i = 0
j = 0

while i < len(nums):
    i = i + 1
    while j < len(nums):        
        #i = i + 1
        if nums[i] + nums[j] == target:
            print(nums[i],nums[j])
        j = j + 1 
    """