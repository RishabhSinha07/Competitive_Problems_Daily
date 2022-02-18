# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        visited = {}
        
        def dfs(root,depth,maxD):
            if root in visited:
                return
            if not root:
                maxD = max(maxD,depth)
                return maxD
            visited[root] = True
            maxD = dfs(root.left,depth+1,maxD)
            maxD = dfs(root.right,depth+1,maxD)
            
            return maxD
        
        z = dfs(root,0,0)
        return z        