class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = nums.count(0)
        
        if count > 1:
            return [0]*len(nums)
        
        total_product = 1
        
        for i in nums:
            if i != 0:total_product*=i
        
        res = []
        
        for i in nums:
            if i == 0:
                res.append(total_product)
            elif count == 0:
                res.append(total_product//i)
            else:
                res.append(0)
                
        return res