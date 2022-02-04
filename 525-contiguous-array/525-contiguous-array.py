class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        data = {0:0}
        
        count, result = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                count-=1
                
            if count in data:
                result = max(result, i-data[count]+1)
            else:
                data[count] = i+1
        
        return result