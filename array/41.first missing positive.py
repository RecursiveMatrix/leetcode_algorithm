# Given an unsorted array, find the smallest missing positive integer
# Example: [1,2,0] --> 3
#          [3,4,-1,1] ---> 2
#          [7,8,9,11,12] ---> 1



# Solution 1:
#     nums.sort()
#     res = 1
#     for num in nums:
#         if num == res:
#             res +=1
#     return res

# Solution 2:

def firstMissingPositive(nums):
    if len(nums) < 1:
        return 1
    elif len(nums) == 1:
        if nums[0] == 1:
            return 2
        else:
            return 1
    else:
        minimum,maximum = min(nums),max(nums)
        if minimum > 1 or maximum < 1:
            return 1
        else:
            for val in range(min(minimum,1),maximum+1):
                if val not in nums:
                    return val
            return maximum+1

print(firstMissingPositive([1,2,0]))




