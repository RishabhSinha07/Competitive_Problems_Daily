# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        a->b->c->d->e : b->a->d->c->e
        
        p1 -> p2.next
        p2 -> p1
        
        '''
        
        if head is None: return None
        
        res = node = ListNode(0,head)
        
        while node:
            p1 = node.next
            if p1 is None:return res.next
            p2 = p1.next
            if p2 is None:return res.next
            temp = p2.next
            p2.next = p1
            p1.next = temp
            node.next = p2
            node = p1
            
        return res.next
        