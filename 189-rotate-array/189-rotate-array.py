class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N, temp = len(nums), [x for x in nums]
        
        for i in range(N):
            pos = (i+k)%N
            nums[pos] = temp[i]
        