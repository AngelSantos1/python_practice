




# Python3 program to find 1's complement of n.
def onesComplement(n):
	v = []
	
	# convert to binary representation
	while (n != 0):
		v.append(n % 2)
		n = n // 2

	v.reverse()

	# change 1's to 0 and 0's to 1
	for i in range(len(v)):
		if (v[i] == 0):
			v[i] = 1
		else:
			v[i] = 0

	# convert back to number representation
	two = 1
	for i in range(len(v) - 1, -1, -1):
		n = n + v[i] * two
		two = two * 2

	return n

# Driver code
n = 22

# Function call
print(onesComplement(n))

# This code is contributed by phasing17






""" numberArray = [3, 5, 2, -4, 8, 11]
#[2, 7, 11, 15]
targetSum = 7

def twoSum(numberArray, targetSum):
    hashTable = {}
    for index in range(len(numberArray)):
        complement = targetSum - numberArray[index]
        #a = numberArray[i+1]
        if targetSum == numberArray[i] + a:
            print(numberArray[i], a)

twoSum(numberArray,targetSum)


print(numberArray.index(7))
 """



""" li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]

temp3 = []
temp4 = 0

for element in li1:
    if element not in li2:
        temp3.append(element)
    if element in li2:
        temp4 +=1

print(temp3)
print(temp4)

 """
""" target = 9
nums = [2, 7, 11, 15]
# [1,2,4,6,7,9]
check = {}

def twoSum(nums, target):
    for i in range(len(nums)):
        if nums[i] in check:
        # print(check(nums(i)), i)
            return nums[i], nums[i]
            # return [check.get(nums[i]), i]
        
        # print([check[nums[i]], (i))
        check[target - nums[i]] = i 

print(twoSum(nums,target))
    
# print(nums[i])
        


 """