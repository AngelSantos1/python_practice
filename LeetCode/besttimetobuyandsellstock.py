# https://leetcode.com/problems/best-time-to-buyLow-and-sellHigh-stock/
""" def MaxProfit(prices):
        max_profit = 0
        for buyLow in range(len(prices) - 1):
            for sellHigh in range(buyLow + 1, len(prices)):
                profit = prices[sellHigh] - prices[buyLow]
                if profit > max_profit:
                    max_profit = profit
        print(max_profit)
        #return max_profit

prices = [7, 1, 5, 3, 6, 4]
MaxProfit(prices) """


""" def maxProfit(prices):
        #buy = prices[0]
        prices = float('inf')
        #min_price = min(prices)
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        print( max_profit)

prices = [7, 1, 5, 3, 6, 4]
maxProfit(prices) """

""" prices = [7, 1, 5, 3, 6, 4]
max_profit = 0
for buyLow in range(len(prices) - 1):
    for sellHigh in range(buyLow + 1, len(prices)):
        profit = prices[sellHigh] - prices[buyLow]
        if profit > max_profit:
            max_profit = profit
print(max_profit) """
""" if prices==[]:
    return() """

def maxProfit(prices):

    
    buy = prices[0]
    max_profit = 0
    
    for day in range(1, len(prices)):
        profit = prices[day] - buy
        
        if profit > max_profit:
            max_profit = profit

        if buy > prices[day]:
            buy = prices[day]
        
    print(max_profit)


prices = [7, 1, 5, 3, 6, 4]


maxProfit(prices)