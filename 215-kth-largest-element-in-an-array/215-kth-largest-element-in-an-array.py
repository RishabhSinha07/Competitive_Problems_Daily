import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlog(n) solution which is stupid
        # nums.sort(reverse=True)
        # return nums[k-1]
        
        # Lets try to get O(nlogk) using heap
        pq = []
        for i in nums:
            heapq.heappush(pq,i)
            
            if len(pq) > k:
                heapq.heappop(pq)
        
        return pq[0]
        