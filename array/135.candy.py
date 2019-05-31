# there are N children standing in a lane, each child is assigned a rating value
# each child should at least be given one candy
# children with a higher rating get more candies than their neighbours
# what is the minimum candies you should give?

def candy(ratings):

    n = len(ratings)
    res = [1 for _ in range(n)]

    # whichever candy number is bigger, add one to the smaller then assign to bigger value
    for i in range(n-1):
        if ratings[i]<ratings[i+1]:
            res[i+1] = res[i] + 1
    for i in range(-2,-n-1,-1):


        if ratings[i]>ratings[i+1]:
            # the maximum of the two is to guarantee the number of candies would not decrease
            res[i] = max(res[i],res[i+1]+1)
    return res

print(candy([1,3,4,5,2]))

