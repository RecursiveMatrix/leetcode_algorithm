# Given an array, rotate the array to the right by k steps, where k is non-negative
# Modify the nums

def rotate(nums,k):

# Solution 1:
    # if k > len(nums):
    #     k -= len(nums)
    # i=0
    # for num in nums[-k:]+nums[:-k]:
    #     print(num)
    #     nums[i] = num
    #     i+=1

# Solution 2:
    def _rotate(end,k):
        if k == 0 or k == end+1:
            return
        for i in range(end-k ,-1, -1):
            nums[i],nums[i+k] = nums[i+k],nums[i]
        _rotate(k-1,k-(end+1)%k)

    k%= len(nums)
    _rotate(len(nums)-1,k)





print(rotate([1,2,3,4,5,6,7],3))
