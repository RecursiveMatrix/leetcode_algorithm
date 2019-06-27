def minPatches(nums,n):

    count,i,upper_bound = 0,0,1

    # upper_bound cannot be reached, hence eaqul needs to be considered
    while upper_bound <= n:

        # range limit comes first
        # the sum of upper_bound and current number can be updated as the new upper bound
        if i<len(nums) and nums[i] <= upper_bound:
            upper_bound += nums[i]
            i += 1

        # the upper_bound needs to be doubled
        else:
            upper_bound <<= 1
            count += 1
    return count



print(minPatches([],7))
