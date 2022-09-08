#Addend (pl. addends) - A number which is added to another

""" def SumOfTwoNumbers(listOfNumbers, targetSumOfAddends):
    listOfNumbers = [2,7,11,15]
    targetSumOfAddends = 9
    for firstAddendInListOfNumbers in range(len(listOfNumbers)-1):
        for secondAddendInListOfNumbers in range(len(firstAddendInListOfNumbers + 1, listOfNumbers)):
            target = targetSumOfAddends == listOfNumbers[firstAddendInListOfNumbers] + listOfNumbers[secondAddendInListOfNumbers]
            if target:

            
            #if firstAddendInListOfNumbers + secondAddendInListOfNumbers == targetSumOfAddends:
                #return (listOfNumbers[firstAddendInListOfNumbers], listOfNumbers[secondAddendInListOfNumbers])

SumOfTwoNumbers(listOfNumbers,targetSumOfAddends) """


def SumOfTwoNumbers(listOfNumbers, targetSum):
    for firstAddend in range(len(listOfNumbers)-1):

        #How do I describe what's happening here -- 'range(firstAddend + 1, len(listOfNumbers))'??
        for secondAddend in range(firstAddend + 1, len(listOfNumbers)):
            
            if listOfNumbers[firstAddend] + listOfNumbers[secondAddend] == targetSum:
                print(listOfNumbers[firstAddend], listOfNumbers[secondAddend])

                #Why does return not work? 
                #return (listOfNumbers[firstAddend], listOfNumbers[secondAddend])
                #return firstAddend, secondAddend

listOfNumbers = [2,7,11,15]
targetSum = 9

SumOfTwoNumbers(listOfNumbers, targetSum)
