# Two strings with same length: answer string: secret , guess string: guess
# If both the position and value match, defined as a bull
# If value matches while position not match, defined as a cow
# return the number of bulls and cows.


def getHint(secret,guess):
    size = len(secret)
    ans_bulls, ans_cows = {}, {}
    bulls, cows = 0, 0

    # calculate the number of bull and record the number of values appear in the rest of the two strings
    for i in range(size):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            if secret[i] not in ans_bulls:
                ans_bulls[secret[i]] = 1
            else:
                ans_bulls[secret[i]] += 1
            if guess[i] not in ans_cows:
                ans_cows[guess[i]] = 1
            else:
                ans_cows[guess[i]] += 1

    # print(ans_bulls,ans_cows)

    for key in ans_bulls.keys():
        # if a key appears in both dict, return the accumulated minimum number of appearance as the number of cows
        if key in ans_cows.keys():
            cows += min(ans_bulls[key],ans_cows[key])

    return '{}A{}B'.format(bulls, cows)

print(getHint('1807','7810'))