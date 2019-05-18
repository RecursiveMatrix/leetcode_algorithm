# Given a string s, find the longest palindromic substring in s
# Assumption: maximum length of s is 1000

# Example: 'babad' --> 'aba' or 'bab'
#          'cbbd' --> 'bb'

def longestPalindrome(s):

    result =''

    for i in range(len(s)):

        # check the pattern such as:'aba'
        # pointer starting from the middle,left = right = 'b'.index()
        temp = find(s,i,i)
        if len(temp)>len(result):
            result = temp

        # check the pattern such as :'abba'
        # pointer starting from 'b' and the following 'b': left = 'b'_left.index(),right = 'b'_right.index()
        temp = find(s, i, i+1)
        if len(temp) > len(result):
            result = temp
    return result


def find(s,l,r):
    # for checking the pattern 'abba',the pointer needs to move two more steps from i, as a result, r<len(s)
    # for 'aba', condition satisfied, 'b'='b',then move pointer
    # for 'abbc', condition satisfied, pointer moves, then not satisfied, pointer moves back.

    while l>=0 and r<len(s) and s[l]==s[r]:

        l-=1
        r+=1
        print(s[l + 1:r])
    return s[l+1:r]

print(longestPalindrome('abba'))