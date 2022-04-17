class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for i in nums:
            if i-1 not in nums:
                start = i-1
                temp = 0
                while start+1 in nums:
                    temp+=1
                    start+=1
                longest = max(longest, temp)
        
        return longest