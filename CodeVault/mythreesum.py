def ThreeSum(listOfNumbers, targetSum):
    #-2
    for firstAddend in range(len(listOfNumbers)):
        for secondAddend in range(firstAddend+1, len(listOfNumbers)):
            #-1
            for thirdAddend in range(secondAddend+1, len(listOfNumbers)):
                if targetSum == listOfNumbers[firstAddend] + listOfNumbers[secondAddend] + listOfNumbers[thirdAddend]:
                    print(listOfNumbers[firstAddend],listOfNumbers[secondAddend],listOfNumbers[thirdAddend])

listOfNumbers = [1,4,45,6,10,8]
targetSum = 22
ThreeSum(listOfNumbers,targetSum)