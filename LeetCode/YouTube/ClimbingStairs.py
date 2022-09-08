#https://www.youtube.com/watch?v=Y0lT9Fck7qI&ab_channel=NeetCode

def climbStairs(totalSteps):
    one, two = 1, 1
    for steps in range(totalSteps - 1):
        temp = one
        one = one + two
        two = temp

    print(one)

totalSteps = 5

climbStairs(totalSteps)
