
def climbStairs(totalSteps):
    combinations = 0
    stepOne = 1
    stepTwo = 1

    for steps in range(totalSteps):
        temp = stepOne
        stepOne = stepOne + stepTwo
        stepTwo = temp
    print(stepOne)

totalSteps = 5

climbStairs(totalSteps)