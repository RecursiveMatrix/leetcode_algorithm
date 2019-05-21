# Given an array of citations(non-negative integer) of a researcher, write a function to compute the researcher's h-index
# H-index is defined as a scientist whose n papers have at least h citations each

# Example: citations = [3,0,6,1,5] --->  output = 3
# Explaination: the researcher has 5 papers with citations 3,0,6,1,5
#               there are 3 papers have been cited no less than 3 times

def hIndex(citations):

    number_of_papers = len(citations)
    citations.sort()
    result = 0


    for nth_paper in range(number_of_papers):

        # filter the paper
        # since the citations has been sorted, (number_of_papers - nth_paper) is the potential value of h-Index
        # this is because the h-Index should be no more than the total number of the paper
        
        if citations[nth_paper] >= number_of_papers - nth_paper:
            result = number_of_papers - nth_paper
            break

    return result

print(hIndex([3,0,6,1,5]))