# Given two non-empty linked lists representing two non-negative integers. The digits
# are stored in reverse order and each of their nodes contain a single digit. Add the
# two numbers and return it as a linked list.

# Explaination: (2->4->3) + (5->6->4) return (7->0->8)
# since 243 + 564 = 708

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

# This class is used to create a ListNode object with two attributes:
# ListNode.val returns the current value
# ListNode.next returns the second (the note after head node) ListNode object


def addTwoNumbers(l1,l2):

    # starting calculate from units digit, since it is in reverse order, the last digit of the result comes from the first node in the nodelist
    valCurr = l1.val + l2.val

    # check out if there is a carry digit, ceiling (1.9-->1)
    up = valCurr // 10

    # create next node using the 10 mode of current node value
    # result keeps track of the first node
    result = answerNode = ListNode(valCurr % 10)

    # moving node to next
    l1 = l1.next
    l2 = l2.next

    # while the two nodes both exits next node:
    while l1 is not None and l2 is not None:

        # next node can be calculated as follows:
        valCurr = l1.val + l2.val + up
        # for the next node, calculate the carry and mode of 10
        up = valCurr // 10
        nextNode = ListNode(valCurr % 10)

        # assign the result to the current node and moving node to next:
        answerNode.next = nextNode
        answerNode = nextNode

        # moving to the next node for l1 and l2
        l1 = l1.next
        l2 = l2.next

    # considering the situation when the length of two nodelist are not same:

    followingNode = None

    # for either of nodelist which still has next node, just attach the rest to the answernode
    if l1 is not None: followingNode = l1
    if l2 is not None: followingNode = l2

    # considering the situation when the carry exits and following node still exits:

    # if there is a carry residual and following node exits:
    while up != 0 and followingNode is not None:

        valCurr = up + followingNode.val
        up = valCurr // 10

        # Attention: Following steps should not be merged, a node object should be defined once to distinguish itself
        # wrong to do the followings:
        # answerNode.next = ListNode(valCurr % 10)
        # answerNode = ListNode(valCurr % 10)

        nextNode = ListNode(valCurr % 10)
        answerNode.next = nextNode
        answerNode = nextNode

        followingNode = followingNode.next

    # if there is a carry residual while following node doesnt exits, just create a new node with carry
    if up != 0 and followingNode is None:

        nextNode = ListNode(up)
        answerNode.next = nextNode
        answerNode = nextNode

    # if there is a carry residual while next node exits, just attach the rest nodes to the answer nodes
    if up == 0 and followingNode is not None:
        while followingNode is not None:
            nextNode = ListNode(followingNode.val)
            answerNode.next = nextNode
            answerNode = nextNode
            followingNode = followingNode.next

    # since we want to return a linked list, we need to return from the first node of the linked list
    return result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(addTwoNumbers(l1,l2).val)
print(addTwoNumbers(l1,l2).next.val)
print(addTwoNumbers(l1,l2).next.next.val)
