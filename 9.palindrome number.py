# Determine whether an integer is a palindrome or not.
# Example: 121 --> True, since from left 121 = 121 from right
#         -121 --> False, since from left -121 != from right 121-
#           10 --> False, since from left 10 != from right 01

def isPalindrome(x):
    # Convert int to str and check if the reverse order is as same as its original order
    x1 = str(x)
    return True if x1 == x1[::-1] else False

print(isPalindrome(6425425235))
print(isPalindrome(254452))