class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)+1
        return (N*(N-1)//2)-sum(nums)