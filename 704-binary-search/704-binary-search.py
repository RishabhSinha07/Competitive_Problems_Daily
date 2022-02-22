class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        while l < r:
            mid = l+(r-l)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        
        if nums[l]==target:
            return l
        return -1