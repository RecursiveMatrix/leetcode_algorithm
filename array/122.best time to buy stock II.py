# Similar to 121
# now many transactions could be completed
# could not sell and buy at the same time
# could not be engaged in multiple transactions


def maxProfit(prices):

    if len(prices) <=1:
        return 0
    else:
        min_p = prices[0]
        profit = 0
        for i in range(1,len(prices)):

            # if price[i] is larger than local minimum value, calculate the profit accordingly
            # or else update the local minimum
            if min_p < prices[i]:
                profit+=prices[i]-min_p
            min_p = prices[i]
        return profit

print(maxProfit([7,1,5,3,6,4]))



