# given a string which only may contain space and letter, return the length of the last word and 0 if not exits

def lengthOfLastWord(s):

    count = 0
    tail = len(s)-1

    # remove all spaces at the end of the string
    while tail >= 0 and s[tail] ==' ':
        tail -= 1

    # if a non space string is detected, start counting
    # when another space appears, end finding string
    while tail>= 0 and s[tail] != ' ':
        tail -=1
        count+=1
    return count


print(lengthOfLastWord('Hello World'))