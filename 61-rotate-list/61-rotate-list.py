# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # At this point we don't know the size of the LL. So we will try to get that and 
        # after getting the size we can basically split the LL from the kth element
        
        # Well not exactlly k, as if we have k > size in that case we want the mod value
        # ie size%k. This is the index where we want to split
        if head is None:
            return None
        
        sizeOfLL, temp = 0, head
        while temp:
            sizeOfLL+=1
            temp=temp.next
        
        # print(f"Size of the LL {sizeOfLL}")
        k%=sizeOfLL
        # print(f"Updated K value is {k}")
        
        if k == 0:
            return head
        
        # Now that we have the size of the LL and the split position, we want to iterate
        # till the position 'k' then assign k.next = null to break the ll and get the k+1
        # element as the return pointer. Now join the kth pointer to the end of return pointer. 
        
        
        return_pointer = None
        
        temp,index = head,1
        while temp:
            if index == sizeOfLL-k:
                return_pointer = temp.next
                temp.next = None
                break
            temp = temp.next
            index+=1
        
        temp = return_pointer
        while temp and temp.next:
            temp = temp.next
        if temp:
            temp.next = head
        
        return return_pointer