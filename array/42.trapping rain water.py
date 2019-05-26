# Given n non-negative integers representing an elevation map where the width of each bar is 1
# compute how much water it is able to trap after raining


# Solution 1:
# def trap(height):
#     h1,h2,ans = 0,0,0
#
#     # h1,h2 will update the maximum value from left and right respectively
#     for i in range(len(height)):
#         h1 = max(h1,height[i])
#         h2 = max(h2,height[-i-1])
#         ans = ans + h1 + h2 - height[i]
#
#     # h1+h2-len(height)*maxh indicates the area of filling water and columns, then minus the area of columns at each point
#     return ans-len(height)*h1


# Solution 2:

def trap(height):
    if len(height) < 2:
        return 0

    # find the heighest position and its index
    max_h, max_h_idx = 0, 0
    for idx, h in enumerate(height):
        if height[idx] > max_h:
            max_h = height[idx]
            max_h_idx = idx
    area = 0

    # from left to heighest position, if less than previous one, update the water, otherwise update the height
    
    tmp = height[0]
    for i in range(max_h_idx):
        if height[i] > tmp:
            tmp = height[i]

        else:
            area += tmp - height[i]

    tmp = height[-1]
    for i in range(len(height) - 1, max_h_idx , -1):
        print(max_h_idx + 1)
        if height[i] > tmp:
            tmp = height[i]
        else:
            area += tmp - height[i]
    return area

print(trap([2,0,2]))