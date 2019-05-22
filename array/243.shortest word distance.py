def shortestDistance(words, word1, word2):

    # set the pointer to -1 since idx starting from 0
    p1 = -1
    p2 = -1
    # set the result to a infinite positive value for return the minimum distance
    res = float("inf")
    for idx, word in enumerate(words):
        # record the index of the two words
        if word == word1 :p1 = idx
        if word == word2 :p2 = idx
        # if the two words both have been found,record the min value of the distance since there could be duplicated elements
        if (p1 != -1 and p2 != -1):
            res = min(res, abs(p1 - p2))
    return res

# print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"],'practice','coding'))
print(shortestDistance(["a",'c','b','a'],'a','b'))