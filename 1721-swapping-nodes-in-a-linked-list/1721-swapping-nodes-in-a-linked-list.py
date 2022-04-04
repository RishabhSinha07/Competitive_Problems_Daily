# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lengthLl(self, ll):
        count = 0
        while ll:
            ll = ll.next
            count+=1
        return count
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        res = head
        length = self.lengthLl(head)
        
        node1 = node2 = None
        current = 0
        while head:
            if current == k-1:
                node1 = head
            elif current == length-k:
                node2 = head
            head=head.next
            current+=1
        
        if node1 and node2:
            node1.val, node2.val = node2.val, node1.val
        
        return res