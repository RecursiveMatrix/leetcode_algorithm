# Given a sorted array, remove duplicates in-place such that each element appear only once and return the new length
# Implement without taking extra space

def removeDuplicates(nums):
    # starting from the second place of the list
    start = 1
    # set another pointer start from the first
    pointer = 0
    size = len(nums)
    # used for record the number of duplicated elements
    counter = 0

    # when the start within the range
    while start < size:
        # when the element is same as the current value, recognized as duplicated element and add counter by 1
        if nums[start] == nums[pointer]:
            counter += 1
        else:
            # when they are not same, assign the new value next to the previous value
            nums[pointer + 1] = nums[start]
            pointer += 1
        start += 1
    # return the original size - number of duplicated element;
    # at the same time, if the length of the given array is 0 or 1, also returns reasonable results
    return size - counter

print(removeDuplicates([1,1,2]))
