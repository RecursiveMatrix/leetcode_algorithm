# given an array for which the ith element is the price of a given stock on day i
# if you were only permitted to complete at most one transaction(buy and sell one share of the stock)
# design an algorithm to find the maximum profit


# dynamic programming, the max_profit = max(previous max profit, current price - min price so fa)
def maxProfit(prices):

    if len(prices) <= 1:
        return 0

    min_price = prices[0]
    max_price = 0

    for i in range(len(prices)):
        # find the local minimum
        min_price = min(min_price,prices[i])
        # calculate the local maximum
        max_price = max(max_price,prices[i] - min_price)

    return max_price

print(maxProfit([7,1,5,3,6,4]))

