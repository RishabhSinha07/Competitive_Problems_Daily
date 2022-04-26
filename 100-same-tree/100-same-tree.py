# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def iot(node, res):
            if node is None:
                return res+'N'
            res+='('
            res = iot(node.left,res)
            res+=str(node.val)
            res = iot(node.right,res)
            res+=')'
            return res
        
        return iot(p,"") == iot(q,"")
    
            