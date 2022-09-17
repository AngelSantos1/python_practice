def maxProfit(prices):
    profit = 0
    temp = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
        #if temp != 0:
        #    profit += temp
            
    return profit

prices = [7, 1, 5, 3, 6, 4]

print(maxProfit(prices))
