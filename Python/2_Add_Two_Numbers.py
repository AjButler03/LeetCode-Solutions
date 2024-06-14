class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# convert linked list to number
def arrToNum(p):
    num = 0 # define variable to store converted number
    dig = 0 # keep track of current digit place
    while p.next != None:
        num = num + (p.val * 10 ** dig) # append digit
        p = p.next # advance pointer
        dig += 1
    num = num + (p.val * 10 ** dig) # grab last digit
    return num


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # convert lists to numbers and calculate sum
        sum = arrToNum(l1) + arrToNum(l2)

        # procede to convert sum into linked list
        # I guess just always try the first one, so that some form of the list is made initially
        l3 = ListNode(sum % 10)
        prev = l3 # use for previous node
        sum = sum // 10 # remove digit from sum
        # procede with other digits
        while (sum > 0):
            temp = ListNode(sum % 10)
            prev.next = temp
            prev = temp # set previous to this node
            sum = sum // 10 # remove digit from sum
        return l3