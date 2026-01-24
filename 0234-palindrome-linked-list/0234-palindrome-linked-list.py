# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow, fast = head, head
        
        #A:
        while fast!= None and fast.next!= None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True