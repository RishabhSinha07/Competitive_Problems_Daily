class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        keep track of the cmax untill it is > 0 if it goes below 0 reset the value
        to 0
        
        [-2,1,-3,4,-1,2,1,-5,4]
        
        max = 6
        cmax = 4-1+2+1 so on
        '''
        max_value = max(nums)
        temp = 0
        for i in nums:
            temp+=i
            max_value = max(max_value,temp)
            if temp < 0:
                temp = 0
                
        return max_value