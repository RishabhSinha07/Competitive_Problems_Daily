# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.height = 0
        
        def dfs(node, height):
            if node is None:
                return node
            self.height = max(height, self.height)
            dfs(node.left, height+1)
            dfs(node.right, height+1)
        
        dfs(root, 1)
        return self.height