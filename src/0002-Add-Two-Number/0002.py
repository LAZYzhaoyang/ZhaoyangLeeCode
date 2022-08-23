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
        res = ListNode()
        root = res
        while (l1 is not None) or (l2 is not None):
            pre = res
            if l1 is not None:
                v1 = l1.val
            else:
                v1=0
            if l2 is not None:
                v2 = l2.val
            else:
                v2=0
            tonext = (v1+v2+res.val)//10
            res.val = (v1+v2+res.val)%10
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
            res.next = ListNode(val=tonext)
            res = res.next
        if res.val==0:
            res = pre
            res.next = None
        return root
