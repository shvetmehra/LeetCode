# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        l = 0
        while curr != None:
            curr = curr.next
            l +=1
        if l == n:
            return head.next
            
        curr = head
        for i in range (l-n-1):
            curr = curr.next

        curr.next = curr.next.next
        return head
        