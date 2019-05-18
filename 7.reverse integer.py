# Given a 32-bit signed integer, reverse digits of an integer.
# Example: input:123 --> output: 321
#          input:-123 --> output:-321
#          input:120 --> output:21

def reverse(x):

    result = 0

    # absolute value of x since we just want to invert the integer, sign doesn't need to be considered at first
    abs_x = abs(x)

    while abs_x !=0:
        # get the integer from the right
        temp = abs_x%10
        # update the result
        result = result*10 + temp
        # truncate the integer
        abs_x //= 10

    # below is for the range of answer required in leetcode
    if x>0 and result <=2**31-1:
        return result
    elif x<0 and result >=-2**31:
        return -result
    else:
        return 0

print(reverse(-49218))