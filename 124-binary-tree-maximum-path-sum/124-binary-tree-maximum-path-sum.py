# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1000
        
        def dfs(node):
            if node is None:
                return 0
            if node:
                l, r = max(0,dfs(node.left)), max(0,dfs(node.right)) 
                temp = node.val+l+r
                self.res = max(self.res,temp)
                return max(l,r)+node.val
            
        dfs(root)
        return self.res
                