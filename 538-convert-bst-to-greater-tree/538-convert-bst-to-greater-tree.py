# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        val = []
        def help1(root):
            if root is None:
                return
            help1(root.left)
            val.append(root.val)
            help1(root.right)
        
        help1(root)
        
        self.temp = 0
        def help2(root):
            if root is None:
                return
            help2(root.right)
            self.temp += val.pop(-1)
            root.val = self.temp
            help2(root.left)
        
        help2(root)
        return root