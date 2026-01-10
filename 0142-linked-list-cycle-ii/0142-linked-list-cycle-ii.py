# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast, pointer = head, head, head

        if head == None or head.next == None:
            return None
        while fast != None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return None
        while pointer != slow:
            pointer = pointer.next
            slow = slow.next
        return slow
        