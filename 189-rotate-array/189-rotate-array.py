# class Solution:
#     # O(n) TC and O(n) SC
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         N, temp = len(nums), [x for x in nums]
        
#         for i in range(N):
#             pos = (i+k)%N
#             nums[pos] = temp[i]
        

class Solution:
    # O(n) TC and O(1) SC
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        
        