class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        data = collections.Counter(nums)
        longest = 0
        
        for i in nums:
            if i-1 not in nums:
                start = i-1
                temp = 0
                while data[start+1]>0:
                    temp+=1
                    start+=1
                longest = max(longest, temp)
        
        return longest