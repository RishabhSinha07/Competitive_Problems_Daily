# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = head = ListNode(0)
        
        while l1 or l2:
            temp = carry
            carry = 0
            
            if l1:
                temp+=l1.val
                l1=l1.next
            if l2: 
                temp+=l2.val
                l2=l2.next
            
            carry = temp//10
            temp = temp%10
            
            head.next = ListNode(temp)
            head=head.next
        
        if carry > 0:
            head.next = ListNode(carry)
        
        return res.next