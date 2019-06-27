# find the longest common prefix, return ''(string) if not found


input = ["flower","flow","flight"]

def longestCommonPrefix(strs):

    result = ''
    word_position = 0

    while strs:

        # go over all the strings in the strs
        for i in range(len(strs)):

            # end if no more corresponding letter was found or there is a mismatch
            if word_position >= len(strs[i]) or strs[0][word_position] != strs[i][word_position]:
                return result
        result+=strs[0][word_position]
        word_position+=1
    return result



print(longestCommonPrefix(input))


