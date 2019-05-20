# There are n people in a party, denoted from 0 to n-1;
# There may or may not only one celebrity in them;
# The celebrity is defined as: The other people knows him while the celebrity doesn't know any of them;
# API : a function 'knows(a,b)' has already predefined which returns boolean to indicate whether a knows b;

# Solution: Each time 'knows(a,b)' was called, a or b can be determined not to be the celebrity;
#           If a knows b, then return True: a cannot be the celebrity since the celebrity is not supposed to know anyone;
#           If a doesn't know b, then return False: b cannot be the celebrity since the celebrity should be known by anyone;
#           A candicate could be selected to be the potential celebrity;
#           Go over from 1 to n-1, assume 0 to be the candidate, whenever a knows b, assign the candidate to b
#           Double check: all n-1 people except the candidate, everyone should know the candidate while the candidate cannot know any of them;
#           Whenever above event happens, return -1 to indicate there is no such celebrity.

def knows(a,b):
#  if a knows b: return True
#  else: return False


def findCelebrity(n):

    candidate = 0

    # no need to consider a group of only one or no person
    if n <= 1:
        return -1

    else:

        for person in range(1,n):
            if knows(candidate,person):
                candidate = person

        for person in range(n):
            if person != candidate:
                if knows(candidate,person) or not knows(person,candidate):
                    return -1

        return candidate


