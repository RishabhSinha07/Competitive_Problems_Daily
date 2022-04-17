# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        data = []
        
        while temp:
            data.append(temp.val)
            temp = temp.next
        
        temp = head
        for i in range(len(data)//2):
            temp.val = data[i]
            temp = temp.next
            temp.val = data[len(data)-i-1]
            temp=temp.next
        
        if len(data)%2 == 1:
            temp.val = data[len(data)//2]
