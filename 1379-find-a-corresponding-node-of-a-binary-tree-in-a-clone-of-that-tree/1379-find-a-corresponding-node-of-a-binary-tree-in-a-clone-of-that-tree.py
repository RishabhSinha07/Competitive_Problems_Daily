# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
# Without duplicates
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(node):
            if node is None:
                return 
            if node.val == target.val:
                return node
            return dfs(node.left) or dfs(node.right)
        
        return dfs(cloned)
"""
# With duplicates
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def deserialize(node, value):
            if node is None:
                value+='N'
                return value
            value+=str(node.val)
            value+='('
            value=deserialize(node.left,value)
            value=deserialize(node.right,value)
            value+=')'
            
            return value
        
        new_target = deserialize(target, "")
        
        def dfs(node):
            if node is None:
                return None
            nonlocal new_target
        
            if deserialize(node,"") == new_target:
                return node
            return dfs(node.left) or dfs(node.right)
            
        return dfs(cloned)