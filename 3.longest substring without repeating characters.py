# Given a string, find the length of the longest substring without repeating characters.

# Explaination: 'abcabcbb' returns 3 since 'abc' is the longest substring without repeating characters.
#               'bbbbbb' returns 1 since 'b' is the longest substring without repeating characters.
#               'pwwkew' returns 3 since 'kew' is the longest substring without repeating characters.

def lengthOfLongestSubstring(s):

    # initiate a dict to store the information with the pattern: key:value --> 'string':updated index
    dict = {}

    # pointer is used for updating the index of the element which appeared before
    # namely, each time a string stored before appears, the pointer will 'reset' for calculating the length of 'new' string
    pointer,ans = 0,0

    # go over all the strings in s:
    for index in range(len(s)):

        # if the index of the string already exists in the dict:
        if s[index] in dict:
            # replace the index of string with the new index:
            # need to update the pointer with the max value of previous index of the same value and pointer itself
            # thinking of the case:'abba'
            pointer = max(dict[s[index]],pointer)
            print('this is the updated index since it appears before: ',pointer)


        # the following two steps are for updating the dict, indicating the lateset index of all stored string

        # if not, calculate the length of the substring
        ans = max(ans,index-pointer+1)
        print('the longest length so far is :',ans)

        # update the index of the current string in the dict, since python counts from 0, should be assigned with 1 plus index
        # besides, in case of the input is '', the answer should be 1 instead of 0
        dict[s[index]] = index+1
        print('the dict is now filled with these: ',dict)
    return ans

lengthOfLongestSubstring('abba')