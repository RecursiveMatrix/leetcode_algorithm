# Similar to 274, the citations have already sorted
# The challenge is to achieve a complexity of log(n)

def hIndex(citations):

    n = len(citations)
    # denote the left and right boundary as the indexes of the citations list

    left,right = 0,n-1

    while left<=right:

        # get the celling result of the mid
        mid = (left + right)//2
        print(mid)
        # assuming mid = left, if the minimum value in citations cannot meet the requirement, move to right by 1
        if citations[mid] < n-mid:
            left = mid + 1
        else:
            right = mid -1

    # by now, left indicates the biggest value that meet the requirement.
    # In other words, finally, left = right = mid;
    # When they are same, just move right boundary, so the maximum left index could be kept

    # better consider based on left, since // will return the nearest left mid
    # besides, if the input is empty, n - left will be 0
    return n - left



hIndex([1,2,2,2,3,3,3])
# print(hIndex([1,2,2,2,3,3,3]))

# print(hIndex([0,1,3,5,6]))


# def hIndex(citations):
#
#     left, right = 0, len(citations)
#     while right > 0:
#         step = right / 2
#         mid = left + step
#         if citations[mid] < len(citations) - mid:
#             left = mid + 1
#             right -= step + 1
#         else:
#             right = step
#     return len(citations) - left

