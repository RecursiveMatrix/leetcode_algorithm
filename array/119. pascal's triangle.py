# Compared to 118, 119 just return a particular row of the triangle
# the rule is : in one row, starting from 1, the next value can be obtained with its previous value
# by (rowIndex-currentIndex)/(currentIndex + 1)



def getRow(rowIndex):

    result = []
    start = 1

    for i in range(rowIndex+1):

        # Attention, the result should be integers
        result.append(int(start))

        # the following part should not be start*= (rowIndex-i)/(i+1)
        # since the division will transfer the result of start to type float
        # need to transfer its type for each calculation

        start = int(start *(rowIndex-i)/(i+1))

    return result
