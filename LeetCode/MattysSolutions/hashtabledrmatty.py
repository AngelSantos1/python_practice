nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    check = {}
    for i in range(len(nums)):
        if nums[i] in check:
            return [check[nums[i]], i]
        check[target - nums[i]] = i

print(twoSum(nums, target))

  