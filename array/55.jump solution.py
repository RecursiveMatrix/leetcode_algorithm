# Given an array of non-negative integers and initially positioned at the first index of the array;
# Each element represents your maximum jump length at that position
# Determine if you could reach the last index


def jumpSolution(nums):

    # test is the maximum
    test = 0
    if not nums:
        return False
    for i in range(len(nums)-1):

        # i indicates how many steps already took if reaches current position
        # at current position i, it can reach as far as nums[i]+i
        # for example,if i = 2,num[2]+2 means if it can reach at position 2, the farest position it can reach.
        test = max(test,i + nums[i])
        # if it cannot reach the current position,return False
        if test <= i:
            return False
    return True

print(jumpSolution([2,3,1,1,4]))
print(jumpSolution([3,2,1,0,4]))
