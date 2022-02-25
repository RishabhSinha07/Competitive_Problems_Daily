class Solution:
    def sortColors(self, nums: List[int]) -> None:
        data = collections.defaultdict(int)
        for i in nums:
            data[i]+=1
        
        res = []
        for i in [0,1,2]:
            res+=[i]*data[i]
        
        for i in range(len(nums)):
            nums[i]=res[i]