# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterate through the LL and create a new head as prev
        # Whenever we find a unique value mark it as curr
        # Attach prev->curr and prev = curr
        # If there are duplicates skip marking the value
        # Return start pointer next (need to have a pointer to this)
        temp = answ = prev = ListNode(-101)
        
        while head:
            if (head and head.next is None and head.val!=prev.val) or (head and head.next and head.val!=head.next.val and head.val!=prev.val):
                temp.next = head
                temp=temp.next
            prev = head
            head=head.next
        
        temp.next = None
        return answ.next