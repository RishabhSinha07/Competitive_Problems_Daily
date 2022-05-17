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
"""
# With duplicates slow
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
"""
# With duplicates fast
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
        self.res = cloned
        
        def dfs(node, value):
            if node is None:
                value += "N"
                return value
            value += str(node.val)
            value += '('
            
            left = dfs(node.left, "")
            right = dfs(node.right, "")
            
            nonlocal new_target
            if left == new_target:
                self.res = node.left
                return
            if right == new_target:
                self.res = node.right
                return
            
            if left is None or right is None:
                return
            
            value+=left
            value+=right
            value+=')'
            return value
        
            
        dfs(cloned, "")
        return self.res