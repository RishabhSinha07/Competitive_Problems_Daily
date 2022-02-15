from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        # TC : O(n) SC : O(n)
        d = defaultdict(int)
        for val in nums:
            d[val]+=1
        for i in d.keys():
            if d[i] == 1:return i
        '''
        nums.sort()
        for i in range(0,len(nums),2):
            if i == len(nums)-1:
                return nums[i]
            if nums[i]!=nums[i+1]:
                return nums[i]
        