# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        start, end = head, head
        flag = False
        while start and end and end.next:
            start = start.next
            end = end.next.next
            
            if start == end:
                flag =True
                break
        
        if flag is False:
            return None
        
        while head and end:
            if head == end:
                return head
            head = head.next
            end = end.next