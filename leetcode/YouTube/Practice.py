depth = {}

def DepthFirstSearch(i,canBuy):
    if i >= len(prices):
        return 0
    
    if (i, canBuy) in depth:
        return depth[(i, canBuy)]
    
    if canBuy:
        buy = DepthFirstSearch(i + 1, not canBuy) - prices[i]
        cooldown = DepthFirstSearch(i + 1, canBuy)