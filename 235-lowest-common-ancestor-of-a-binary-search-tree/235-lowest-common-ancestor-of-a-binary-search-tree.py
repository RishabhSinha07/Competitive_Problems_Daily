# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p is None or q is None:
            return None
        
        l = min(p.val,q.val)
        r = max(p.val,q.val)
        
        def dfs(node, l, r):
            if node is None:
                return
            if l <= node.val <= r:
                return node
            if node.val > l and node.val > r:
                return dfs(node.left, l, r)
            if node.val < l and node.val < r:
                return dfs(node.right, l, r)
        
        
        return dfs(root, l, r)