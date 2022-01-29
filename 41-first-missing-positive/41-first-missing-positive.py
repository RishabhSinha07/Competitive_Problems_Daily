class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Method 1 
        # TC : O(n) 
        # SC : O(n)
        '''
        data = collections.defaultdict(int)
        for i in nums:
            data[i]+=1
        
        for i in range(1,2**32):
            if data[i]==0:
                return i
        '''
        
        # Method 2
        '''
        - If the maximun of the nums < 0 -> result = 1
        - If all the values in range 1 to max is present -> result = max+1
        - If value is missing return the value
        TC : O(n)
        SC : O(1)
        '''
        
        max_value = max(nums)
        if max_value <= 0:
            return 1
        temp = set(nums)
        for i in range(1,max_value):
            if i not in temp: return i
        
        return max_value+1