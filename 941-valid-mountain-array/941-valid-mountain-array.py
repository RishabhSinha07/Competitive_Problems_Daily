class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
#         N = len(arr)
#         left, right = 0, N-1
        
#         while left < N-1 and arr[left]<arr[left+1]:
#             left+=1
        
#         while right > 0 and arr[right]<arr[right-1]:
#             right-=1
        
#         print(left,right)
#         return left==right and left!=0 and right!=N-1
    def validMountainArray(self, a: List[int]) -> bool:
        start, end, L = 0, -1, len(a)

        while start < L-1 and a[start] < a[start+1]: 
            start += 1
        while end > -L and a[end] < a[end-1]: 
            end -= 1

        return start == end + L and 0 < start and end < -1