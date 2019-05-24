# prices: list --> similar to 121 and 123
# find the maximum profit within at most two transactions
# could not get engaged in multiple transactions at the same time, buy before you sell


# buy1 indicates: the minimum price so far
# always update the minimum price so far, which represents the opportunity to buy in

# sell1 indicates: the maximum profit one can make so far for one transaction
# from the nearest minimum price to the current position, the most profit the buyer could have

# buy2 indicates: money you want to buy in now considering previous transaction.
#
# (if the profit keeps increasing, buy2 will not change, since it will be worth remain the same)
# keep tracking the most profit and checking if it is worth for the next invest




def maxProfit(prices):
    if len(prices) < 2:
        return 0

    buy1 = buy2 = float('inf')

    sell1 = sell2 = -float('inf')
    # sell1一直记录赚钱最多的那个cycle
    for i in range(len(prices)):
        buy1 = min(buy1, prices[i])
        sell1 = max(sell1, prices[i]-buy1)
        print(buy1,sell1)

        buy2 = min(buy2, prices[i]-sell1)
        sell2 = max(sell2, prices[i]-buy2)
        print(buy2,sell2)
        print('\n')


    return sell2

print(maxProfit([5,10,3,14,1,8]))