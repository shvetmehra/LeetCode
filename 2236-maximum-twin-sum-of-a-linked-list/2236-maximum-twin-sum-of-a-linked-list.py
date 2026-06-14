# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    # Reverse the linked list which is starting at Slow.
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        maxSum = 0
        firstHalf = head
        secondHalf = prev
        while secondHalf:
            maxSum = max(maxSum, firstHalf.val + secondHalf.val)
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return maxSum
        