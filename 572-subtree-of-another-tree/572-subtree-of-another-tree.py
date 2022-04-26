# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sub(node, t):
            if node is None:
                t+='N'
                return t
            t+='('
            t = sub(node.left,t)
            t += str(node.val)
            t = sub(node.right,t)
            t+=')'
            
            return t

        subRoot = sub(subRoot,'')
        self.res = False
        
        def check(node, t, subRoot):
            if node is None:
                t+='N'
                return t
            temp = ""
            temp +='('
            temp = check(node.left,temp,subRoot)
            temp += str(node.val)
            temp = check(node.right,temp,subRoot)
            temp +=')'
            
            if temp == subRoot:
                self.res = True
            
            t+=temp
            return t
        
        check(root,"",subRoot)
        return self.res