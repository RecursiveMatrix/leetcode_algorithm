# prices similar to 121,122,123
# now given the maximum number of transaction allowed k, to return the maximum profit
# The problem could be decomposed of the previous 3 problems


def maxProfit(prices,k):

    # Situation 1: if k = 0 or the length of prices < 2, transaction could not even been done.
    if len(prices)<2 or k<1:
        return 0

    # Situation 2: if k is too large, the problem becomes problem 122, namely, no transaction limited
    elif len(prices)//2 <= k:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:
                profit += prices[i] - prices[i-1]
        return profit

    # Situation 3: dynamic programing
    else:

        # create a bunch of infinite numbers for k transactions
        buy = [float('inf') for _ in range(k)]
        sell = [float('-inf') for _ in range(k)]

        # for all prices, find the global minimum price and maximum profit earned from one transaction so far
        for idx,price in enumerate(prices):

            # This is to reveal how buy and sell change:
            # buy[0] is the local minimum of price so far;
            # sell[0] is the local maximum profit for one transaction so far;
            buy[0] = min(buy[0],price)  # compare the first price with each price in the list, update to the lowest price by now
            sell[0] = max(sell[0],price - buy[0]) # compare the profit ever sold with the profit by now, update to the highest profit for one transaction by now


            # after knowing what is the minimum price and the maximum profit so far, update each transaction
            for i in range(1,k):

                # all buy[i] and sell[i] are same as buy[0] and sell[0] if the price keeps increasing;
                # buy[i] and sell[i] will be updated when price goes down;
                # buy[i] indicates: guarantee the maximum profit, if one wants to buy in at current position, the money needs to pay
                # update buy[i] using last transaction sell[i]
                # sell[i] indicates: the k th maximum profit in one transaction 
                buy[i] = min(buy[i],price-sell[i-1])
                sell[i] = max(sell[i], price-buy[i])


            print('buy.{}.time:'.format(idx+1),buy)
            print('sell.{}.time:'.format(idx+1),sell)
            print('\n')
        return sell[-1]

# print(maxProfit([2,3,4,10,3,9,3,1,5,7,8,6],4))

# print(maxProfit([2,3,4,10,3,9],4))



