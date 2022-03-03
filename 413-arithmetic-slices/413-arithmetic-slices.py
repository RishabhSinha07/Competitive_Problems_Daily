class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Loop for each element in range 0 to len(nums)-2
        # For each pair untill the diff is same insert the subarray into the res if len>=3
        # Else break
        # TC : O(n^2)
        # SC : O(1)
        
        
        if len(nums) < 3: return 0
        
        result = 0
        for i in range(0,len(nums)-1):
            temp, diff = [i], nums[i]-nums[i+1]
            for j in range(i,len(nums)-1):                
                if nums[j]-nums[j+1] == diff:
                    temp.append(j+1)
                    if len(temp) >= 3:result+=1
                else:
                    break
        
        return result
                    
                
                
            
        
        
        
        