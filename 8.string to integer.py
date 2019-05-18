def myAtoi(str):

    num = ''
    found = False
    negative = False
    index = 0
    # get rid of spaces
    s = str.strip()
    legalnum = '1234567890'
    legalmark = '-+'

    # structure:
    # check the length of given string after getting rid of space:
    #       if it is 0, return 0;
    #       if it is 1, if it is '-'or'+': return 0;
    #                   if it is a number, just return int(s);
    #       if it is >=1, if the first is '-'or'+' and second is a number: found and start from the second string;
    #                               if the first is '-': indicate it is a negative number;
    #                     if the first is a number: found however starting from the beginning;
    #                     else: return 0
    #                     while found and index is within range:
    #                               check if it is a number and concatenate all the numbers
    #                                     if it is not a number, then finish finding the number
    # return answer accordingly:
    # if it is negative:
    #       if it is within range: return -num, otherwise return 0
    # if it is not negative:
    #       if it is within range: return num, otherwise return 0
    # else: return 0
    #
    if len(s) == 0:
        return 0

    elif len(s) ==1:
        if s in legalnum:
            return int(s)
        else:
            return 0

    elif len(s)>1:
        if s[0] in legalmark and s[1] in legalnum:
            found = True
            index = 1
            if s[0] == '-':

                negative = True

        elif s[0] in legalnum:
            found = True

        else:
            return 0
        while found and index<=len(s)-1:
            if s[index] in legalnum:
                num += s[index]
                index += 1

            else:
                found = False

        num = int(num)

    if negative is True:
        if -num <= -2**31:
            return -2**31
        else:
            return -num

    elif negative is False:
        if num >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        return num
    else:
        return 0

print(myAtoi(' -42'))