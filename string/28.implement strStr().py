# find the needle in haystack, return the position of the needle or -1 if not found


def strStr(haystack,needle):

    size1 = len(haystack)
    size2 = len(needle)

    # caution to the limit range of index
    for i in range(size1-size2+1):
        if haystack[i:i+size2] == needle:
            return i

    return -1

print(strStr('mississippi','pi'))