# Given an array nums containing n+1 integers where each integer is between 1 and n.
# at least one duplicate number must exist, assume there is only one duplicate number

def findDuplicate(nums):

    # since 0 is not in the list, starting from the 0 as a head of a linked list
    slow, fast = 0, 0
    while True:

        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    result = 0
    while True:
        
        result = nums[result]
        slow = nums[slow]

        if slow == result:
            return result

print(findDuplicate([1,3,4,2,2]))