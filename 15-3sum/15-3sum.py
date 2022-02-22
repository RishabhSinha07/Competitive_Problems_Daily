class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1] : continue
                
            target = -nums[i]
            beg = i+1
            end = len(nums)-1
            while beg < end:
                if nums[beg] + nums[end] == target:
                    result.append((nums[i],nums[beg],nums[end]))
                    beg +=1
                    end -=1
                    continue
                if nums[beg] + nums[end] > target :
                    end-=1
                    continue
                if nums[beg] + nums[end] < target :
                    beg+=1
            
        
        return set(result)