# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.li = []
        
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.li.append(node)
            dfs(node.right)
        
        dfs(root)
        
        v1 = self.li[0]
        v2 = self.li[-1]
        
        for i in range(len(self.li)-1):
            if self.li[i].val > self.li[i+1].val:
                v1 = self.li[i]
                break
                
        for i in range(len(self.li)-1,0,-1):
            if self.li[i].val < self.li[i-1].val:
                v2 = self.li[i]
                break
                
        v1.val, v2.val = v2.val, v1.val