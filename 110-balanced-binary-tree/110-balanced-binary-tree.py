# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        
        def dfs(node):
            if node is None or self.flag == False:
                return 0
            
            lc = dfs(node.left)
            rc = dfs(node.right)
            
            if abs(lc-rc) > 1:
                self.flag = False
                
            return max(lc,rc)+1
        
        dfs(root)
        return self.flag
        
            