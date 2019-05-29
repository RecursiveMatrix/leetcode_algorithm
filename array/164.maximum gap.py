# Given an unsorted array, find the maximum difference between the successive elements in its sorted form
# return 0 if containing less 2 elements

def maximumGap(nums):
    if len(nums) < 2:
        return 0



    # create n+1 bucket to ensure there at least one empty
    else:
        n = len(nums)
        min_b = [0 for _ in range(n + 1)]
        max_b = [0 for _ in range(n + 1)]
        has_b = [False for _ in range(n+1)]
        max_bi = max(nums)
        min_bi = min(nums)

    # This is to ensure the index not to be 0
        if max_bi == min_bi:
            return 0

    # min_b means all minimum value for each bucket
    # max_b means all maximum value for each bucket
    # for eaample. if in a bucket, there are two numbers, the minimum will be in the min_b while maximum will be in max_b
    # however for most time, there are only one number, so the value of the two are same
    # once put the number in the bucket, set the tag to True
        for num in nums:
            index = int((num - min_bi) * n / (max_bi - min_bi))
            min_b[index] = num if not has_b[index] else min(num, min_b[index])
            max_b[index] = num if not has_b[index] else max(num, max_b[index])
            has_b[index] = True

    # max_b[0] is the maximum value of the first bucket
    # finding the biggest difference between the minimum value of the bucket and the maximum value before that
        print(min_b)
        print(max_b)
        res = 0
        m = max_b[0]
        for i in range(1, n + 1):
            if has_b[i]:
                gap = min_b[i] - m
                print(gap)
                if gap > res:
                    res = gap

                m = max_b[i]
        return res

print(maximumGap([1,4,6,10]))

    