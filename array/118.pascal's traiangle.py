# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle

# Example: input = 5
# Output: [
#   [1],
#   [1,1],
#   [1,2,1],
#   [1,3,3,1],
#   [1,4,6,4,1]
#]

def generate(numRows):

    result = []

    # generate the frame of the Pascal's triangle with all values equal to 1
    for i in range(numRows):
        row = [1] * (i+1)

        # starting from the third row:
        if i >= 2:
            # go over all values in a row except the first and last values.
            for n in range(1,i):
                # update the value according to the rule.
                row[n] = pre[n-1]+pre[n]

        result += [row]

        # once finish updating one row, assign it to the previous row for recursive part.
        pre = row

    # a more friendly way to show results
    for content in result:
        print(content)

    return result

print(generate(10))