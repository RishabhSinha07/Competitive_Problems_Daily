class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = collections.defaultdict(int)
        
        for i in nums:
            data[i]+=1
        
        result = len(nums)/2
        key = -1
        
        for keys,value in data.items():
            if value > result:
                result = value
                key = keys
        
        return key