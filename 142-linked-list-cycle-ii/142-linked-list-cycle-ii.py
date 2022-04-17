# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        temp = {}
        while head and temp.get(head) != 1:
            temp[head]=1
            head = head.next
        if head:
            return head
        return None