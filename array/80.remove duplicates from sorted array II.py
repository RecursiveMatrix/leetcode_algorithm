# Similar to NO.27 question
# now needs to record the duplicates twice

def removeDuplicate(nums):
    start = 1
    pointer = 0

    # switch is used for indicating if the duplicate part contains more than 2 elements
    switch = False
    size = len(nums)
    # count used for recording the number of digits
    count = 0

    # attention to the range of index!
    if size <= 1:
        return size


    else:
        while start < size:

            # if a duplicated element is found and less than 2
            if nums[start] == nums[pointer] and not switch:
                nums[pointer + 1] = nums[pointer]
                switch = True
                count += 1
            elif nums[start] != nums[pointer]:
                # if a different element is found and such element has been found its duplicate before
                if switch:
                    pointer += 2
                    switch = False
                else:
                    pointer += 1

                nums[pointer] = nums[start]
                count += 1

            start += 1

        # return detailed result instead of just the length
        return nums[:count + 1]


print(removeDuplicate([1,2,3,3,3,4,5,6,7,7,7,8,8,8,9,9,10,11,12,13,13,13,13]))