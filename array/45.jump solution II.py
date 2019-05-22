# Given an array of non-integers, initially positioned at the first index of the array
# Each element in the array represents your maximum jump length at that position
# Now the goal is to reach the last index in the minimum of jumps

# starting from 0;
# for the range of th (i+1)th jump:
# the farest position the ith jump could reach to the maximum reach for all position within ith jump could reach
# if the farest reach of the ith jump could reach the end of the list, then quit loop


def jumpSolution(nums):

    start = 0
    step = 0
    reach = 0
    if len(nums) <= 1:
        return 0
    else:
        # check if last ith jump could reach the last point:
        while reach < len(nums) - 1:
            farest = 0
            # for the ith jump, the range starting from start to reach
            for i in range(start, reach + 1):
                print('start:',start,'reach:',reach,'ith:',i)
                # find the farest ranges for all possible position within ith jump
                farest = max(farest, nums[i] + i)
                print('farest:',farest)
            start = reach + 1
            print('start:',start)
            reach = farest
            print('reach:',reach)
            step += 1
    return step

print(jumpSolution([2,3,1,1,4]))
