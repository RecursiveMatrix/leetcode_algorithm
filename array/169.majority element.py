# Given an array of size n, find the majority element.
# The majority element is the element that appears more than n/2 times
# assume the majority always exists and the array is not empty


# Solution 1(should work in python however not accepted when submitting on line)
# def majorityElement(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     dict = {}
#     for number in range(len(nums)):
#         if nums[number] not in dict:
#             dict[nums[number]] = 1
#         else:
#             dict[nums[number]] += 1
#     print(dict)
#     for i in dict.keys():
#         if dict[i] >= len(nums) / 2:
#             return i
#
# print(majorityElement([3,2,3]))

# Solution 2
# def majorityElement(nums):
#
#     cnt, ret = 0, 0
#     for num in nums:
#         if cnt == 0:
#             ret = num
#         if num != ret:
#             cnt -= 1
#         else:
#             cnt += 1
#     return ret
#
# print(majorityElement([2,2,1,1,1,2,2]))

# Solution 3
# def majorityElement(nums):
#
#
#     a = set(nums)
#     for num in a:
#         # count the number of current value in the given array
#
#         if nums.count(num) > len(nums) // 2:
#
#             return num
#
# print(majorityElement([3,2,3]))