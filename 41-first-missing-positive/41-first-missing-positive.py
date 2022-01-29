class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        data = collections.defaultdict(int)
        for i in nums:
            data[i]+=1
        
        for i in range(1,2**32):
            if data[i]==0:
                return i