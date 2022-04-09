class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        li = []
        for i in list(set(nums)):
            li.append((-counter[i],i))
        heapq.heapify(li)
        
        return [heapq.heappop(li)[1] for _ in range(k)]
        
            