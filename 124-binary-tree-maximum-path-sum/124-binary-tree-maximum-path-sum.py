# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        
        def dfs(root):
            if root is None:
                return 0
            
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))
            
            temp = left+right+root.val
            nonlocal max_sum
            max_sum = max(max_sum,temp)
            return max(left, right)+root.val
        
        dfs(root)
        return max_sum