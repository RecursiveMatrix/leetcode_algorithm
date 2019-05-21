# Similar to 169, now needs to find all numbers which appears more than n/3
# complexity should be o(n) and space o(1)


# Solution 1 :a similar approach: space requirement not meets
# def majorityElement(nums):
#     dict = {}
#     answer = []
#     for number in nums:
#         if number in dict:
#             dict[number] += 1
#         else:
#             dict[number] = 1
#     for key in dict.keys():
#         if dict[key] > len(nums) / 3:
#             answer.append(key)
#     return answer

# Solution 2 :
# def majorityElement(nums):
#     answer = []
#
#     for i in set(nums):
#         if nums.count(i) > len(nums) / 3:
#             answer.append(i)
#     return answer




