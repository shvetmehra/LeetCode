# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        small, large = ListNode(0), ListNode(0)
        smallp, largep = small, large

        while head != None:
            if head.val<x:
                smallp.next = head
                smallp = smallp.next
            else: 
                largep.next = head
                largep = largep.next
            head = head.next
        
        smallp.next = large.next
        largep.next = None
        return small.next

        
        