# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.result = 0
        
        def dfs(node, max_value):
            if node is None:
                return
            if node.val >= max_value:
                self.result+=1
            temp = max(max_value, node.val)
            dfs(node.left, temp)
            dfs(node.right,temp)
        
        dfs(root, -float('inf'))
        return self.result