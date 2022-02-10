class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        data = collections.defaultdict(int)
        data[0]=1
        cSum = 0
        count = 0 
        for i in nums:
            cSum+=i
            count+=data[cSum-k]
            data[cSum]+=1
        return count
    
    