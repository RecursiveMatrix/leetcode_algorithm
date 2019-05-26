# Given an unsorted array return whether an increasing subsequence of length of 3 exists or not in the array
# if there exists i,j,k such that arr[i]<arr[j]<arr[k] given 0<=i<j<k<=n-1
# the three elements may not be consecutive

# go over the list and update the minimum and maximum value so far
# whenever a new maximum is found, the triplet subsequence exists

def increasingTriplet(nums):

    min_sofar = float('inf')
    max_sofar = float('inf')

    size = len(nums)

    if size < 3:
        return False

    else:
        for num in nums:

            if num < min_sofar:
                min_sofar = num
            elif num > max_sofar:
                return True
            elif num > min_sofar and num <= max_sofar:
                max_sofar = num

        return False

print(increasingTriplet([2,5,3,6,1,9]))