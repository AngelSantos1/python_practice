# https://leetcode.com/problems/best-time-to-buyLow-and-sellHigh-stock/
def MaxProfit(prices):
        max_profit = 0
        for buyLow in range(len(prices) - 1):
            for sellHigh in range(buyLow + 1, len(prices)):
                profit = prices[sellHigh] - prices[buyLow]
                if profit > max_profit:
                    max_profit = profit
        print(max_profit)
        #return max_profit

prices = [7, 1, 5, 3, 6, 4]
MaxProfit(prices)



""" prices = [7, 1, 5, 3, 6, 4]
max_profit = 0
for buyLow in range(len(prices) - 1):
    for sellHigh in range(buyLow + 1, len(prices)):
        profit = prices[sellHigh] - prices[buyLow]
        if profit > max_profit:
            max_profit = profit
print(max_profit) """


