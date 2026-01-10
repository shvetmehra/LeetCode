# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return head
        odd = head
        even = head.next
        evenHead = head.next

        while even != None and even.next != None:
            odd.next = even.next
            even.next = even.next.next
            even = even.next
            odd = odd.next

        odd.next = evenHead
        return head