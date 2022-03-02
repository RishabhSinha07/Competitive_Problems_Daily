class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                left+=1
                continue
            break
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>=nums[i-1]:
                right-=1
                continue
            break
        
        if left > right:
            return 0
        
        min_value = min(nums[left:right+1])
        max_value = max(nums[left:right+1])
        
        for i in range(left,-1,-1):
            if nums[i]>min_value:
                left=i
                continue
            break
        
        for i in range(right,len(nums)):
            if nums[i]<max_value:
                right=i
                continue
            break
        
        return right-left+1
        