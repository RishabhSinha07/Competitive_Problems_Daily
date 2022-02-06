class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        count = collections.defaultdict(int)
        
        for i in nums:
            count[i]+=1
            if count[i] <= 2:
                nums[pos]=i
                pos+=1
        
        return pos