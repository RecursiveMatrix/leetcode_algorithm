# Given an array and a value, remove all instances of that value in-place and return the new length
def removeElement(nums,val):

    start = 0
    size = len(nums)
    while start<size:

        # when current value meets requirement, switch all the way to the back
        if nums[start] == val:
            nums[start] = nums[size-1]
            # truncate the list to remove the element
            size -=1
        start +=1
    return size


print(removeElement([1,2,4,5,3],2))
