# Given an array for which the ith element is the price of a given stock on day i
# calculate the maximum profit
# complete as many as transactions, however, sell before buy
# once sell, cannot buy for the next day. Namely, if it is cooling down on day i, there must be a sell in day i-1

# dynamic programming:
# if it is not engaged in transaction on day i, denote as profit[i][0]
# if it is engaged in transaction in on day i, denote as profit[i][1]
# if there is a cooldown on day i, denote as profit[i][2]
# the value above indicate the maximum profit so far

# updating:
# on day i, if it is not engaged in transaction, namely, profit[i][0]:
#           previous day i-1 it is not engaged in transaction, the profit will be the same
#           or , the previous day i-1, it is in the state of cooldown, the profit will be the same
#           finally, update the maximum value of the above two

# on day i, if it is engaged in transaction, namely, profit[i][1]:
#           previous day i-1, depending on it it is engaged in transaction, the profit will be the maximum value of the following two:
#           1. engaged on day i-1, since the local profit may be decreased on day i
#           2. not engaged on day i-1, calculated as: maximum profit earned on day i-1, minus the prices[i] on day i

# on day i, it is cooldown, indicating that on day i-1, it is in the state of sell, or engaged in transaction.
#           hence the profit[i][2] should be updated by the profit on day i-1: profit[i-1][1]

# the final state should not be engaged in transaction to obtain a maximum profit
# In summary:
# 0 ---> 0: not buy in
# 2 ---> 0: not buy in after cooldown
# 0 ---> 1: buy in, profit could be decreased
# 1 ---> 1: not sell
# 1 ---> 2: sell then become cooldown


def maxProfit(prices):

    # if not prices:
    #
    #     return 0
    #
    # else:
    #     n = len(prices)
    #     profit = [[0]*3 for _  in range(n)]
    #     profit[0][0],profit[0][1],profit[0][2] = 0,-prices[0],0
    #     for i in range(1,len(prices)):
    #         profit[i][0] = max(profit[i-1][0],profit[i-1][2])
    #         profit[i][1] = max(profit[i-1][1],profit[i-1][0]-prices[i])
    #         profit[i][2] = profit[i-1][1] + prices[i]
    #     return max(profit[n-1][0],profit[n-1][2])


    n = len(prices)
    if n < 2:
        return 0
    else:

        # The following three indicate: the maximum profit when the nearest previous state is sell, buy or cooldown.
        sell = [0 for _ in range(n)]
        buy = [0 for _ in range(n)]
        cooldown = [0 for _ in range(n)]
        buy[0] = -prices[0]

        for i in range(1,n):

            # 1. if sell[i] = sell[i-1], it means there is no difference to sell on day[i] or day[i-1],
            #   which means day i is cooldown day.
            # 2. if sell[i] = prices[i] + buy[i-1],it means literally sell stock on day i,
            # since buy[i] is defined as a negative number as negative profit or just the profit for such buy
            sell[i] = max(sell[i-1],prices[i]+buy[i-1])

            # 1. if buy[i] = buy[i-1], it means there is no different to buy on day[i] or day[i-1].
            #   which means there is no action on day i, or, the profit keeps increasing.
            # 2. if buy[i] = cooldown[i-1] - prices[i], this means that you start to buy in at current time,
            #   the profit then will be updated with the previous sold cooldown - current price[i] since buy in
            #   will lose money
            buy[i] = max(buy[i-1],cooldown[i-1]-prices[i])

            # cooldown can only happen after sell
            cooldown[i] = sell[i-1]
        print(sell)
        print(buy)
        print(cooldown)
        return sell[-1]







print(maxProfit([1,2,3,0,2]))