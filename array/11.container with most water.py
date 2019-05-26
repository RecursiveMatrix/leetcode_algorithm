# Given n non-negative integers, where represent a point at coordinate(i,ai)
# n vertical lines are drawn such that the two endpoints of line i is at (i,ai) and (i,0)
# find two lines so that together with x-axis forms a container containing the most water

# define two pointers then narrow down to the middle, record the maximum value of area ever recorded

def maxArea(height):

    left, right =0, len(height)-1
    maxarea = 0

    while left<right:
        width = right-left
        if height[left]<height[right]:
            cur_height = height[left]
            left+=1
        else:
            cur_height = height[right]
            right-=1

        cur_area = width*cur_height
        maxarea = max(maxarea,cur_area)

    return maxarea

print(maxArea([1,8,6,2,5,4,8,3,7]))

