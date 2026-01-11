# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow, fast = head, head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

        # The reversal Part

        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Calculating the Sum

        max_sum = 0
        firstHalf = head
        secondHalf = prev

        while secondHalf:
            twinSum = firstHalf.val + secondHalf.val
            max_sum = max(twinSum, max_sum)
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return max_sum