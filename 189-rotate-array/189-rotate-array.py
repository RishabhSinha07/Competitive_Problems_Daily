class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums)-k%len(nums)
        for i,j in enumerate(nums[k:]+nums[:k]):
            nums[i]=j
        