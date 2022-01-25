class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums = [1,2,3,4]
        
        1.  we can iterate from l to right and update the value in the result arr. 
            The updation is:
            res = [1,1,1,1]
            upd = [1,1,2,6] ie arr[i] = arr[i]*curr product
        
        2.  we can iterate from r to left and update the value in the result arr. 
            The updation is:
            res = [1,1,2,6]
            upd = [24,12,8,3] ie arr[i] = arr[i]*curr product
        
        '''
        N = len(nums)
        result = [1]*N
        
        curr = 1
        for i in range(N):
            if i != 0:
                result[i]*=curr
            curr*=nums[i]
        
        curr = 1
        for i in range(N-1,-1,-1):
            if i != N-1:
                result[i]*=curr
            curr*=nums[i]
        
        return result