# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.count = 0
        self.value = 0
        
        def dfs(node):
            if node is None or self.count > k-1:
                return
            dfs(node.left)
            if self.count <= k-1:
                self.count+=1
                self.value = node.val
            dfs(node.right)
            
        dfs(root)
        return self.value