# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        track, data = [], collections.defaultdict(list)
        
        for i in lists:
            while i:
                heapq.heappush(track,i.val)
                i=i.next
                
        res = temp = ListNode(0)
        while len(track) > 0:
            temp.next = ListNode(heapq.heappop(track))
            temp = temp.next
        
        return res.next
            