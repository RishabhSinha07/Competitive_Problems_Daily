# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        data1 = {}
        
        while headA:
            data1[headA]=1
            headA=headA.next
        
        while headB:
            if data1.get(headB):
                return headB
            headB=headB.next