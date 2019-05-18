# A string is written in a zigzag pattern on a given number of rows:
# Example: PAYPALISHIRING , ROWS = 3, output --> PAHNAPLSIIGYIR
#   P   A   H   N
#   A P L S I I G
#   Y   I   R

def convert(s,numRows):

    # initiate several strings in the result list
    result = [''for i in range(numRows)]
    # define the first row is 0, step for going up or down
    row, step = 0,1

    # for all strings in s:
    for string in s:
        # store the string in the row position
        result[row] += string

        # if it is now in the first row, or row ==0, it means needs to going down, step =1
        if row ==0:
            step =1
        # if the row reaches the bottom, the row should go up, then step = -1
        elif row == numRows-1:
            step = -1

        # update the row, or the position of desired place to store the string
        row += step

    # concatenate all the result
    return ''.join(result)

print(convert('paypalishiring',3))
