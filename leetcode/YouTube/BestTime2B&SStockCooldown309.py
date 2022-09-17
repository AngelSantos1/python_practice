def MaxProfit(prices):
    # State: canBuy or Selling?
    # If Buy -> i + 1
    # If Sell -> i + 2
    depth = {} # key=(i, canBuy) val=max_profit
    
    # i = Index, canBuy = TypeBoolean (True || False)
    def DepthFirstSearch(i,canBuy):
        
        #Base Case - Prevent Out of Bounds
        if i >= len(prices):
            return 0
        
        # If MaxProfit Computed/Stored Before Return Value
        if (i, canBuy) in depth:
            return depth[(i, canBuy)]
        
        # Buying State
        if canBuy:
            buy = DepthFirstSearch(i + 1, not canBuy) - prices[i]
            cooldown = DepthFirstSearch(i + 1, canBuy)
            # Cache result
            depth[(i, canBuy)] = max(buy, cooldown)
        
        # Selling State
        else:
            sell = DepthFirstSearch(i + 2, not canBuy) + prices[i]
            cooldown = DepthFirstSearch(i + 1, canBuy)
            depth[(i, canBuy)] = max(sell, cooldown)
            
        return depth[(i, canBuy)]
    
    return DepthFirstSearch(0, True)
    
    """ max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:
            cooldown
            
        if prices[i] > prices[i-1]:
            buy = prices[i-1]
            if buy 
            sell = prices[i] - prices[i-1] """
            


prices = [1, 2, 3, 0, 2]
print(MaxProfit(prices))