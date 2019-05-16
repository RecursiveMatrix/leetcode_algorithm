# Given an array of integers, return indices of the two numbers such that they add up to a specific target
# Assum each input would have exactly one solution, same element cannot be used twice
# Example: nums = [2,7,11,15], target = 9
# Explanation: nums[0] + nums[1] = 2 + 7 = 9, return [0,1]

# Hash Table

def twoSum(nums,target):

    dict = {}

    # for all index in nums:
    for index in range(len(nums)):

        # if the element can be found in dict:
        if nums[index] in dict:
            # return the index previously stored in dict, and the current index
            return dict[nums[index]],index

        # if the element cannot be found in dict:
        else:
            # store the target element using the following pattern in the dict: key:value --> target element:current index
            dict[target-nums[index]] = index

# test:
print(twoSum([3,3],6))
# Complexity: n
# Related knowledge:
# 1. given a list, return the index with corresponding value: listname.index(value)
#    However, there could be problem when two same elements in the list
#    listname.index(str,start_index=0,end_index=len(listname))

# 2. in or not in dict, check all the values in dict to see if the given value is in the dict values
#    Hash Table in python is implemented using dict type object

# 3. adding a value to a dict: dict[key] = value

