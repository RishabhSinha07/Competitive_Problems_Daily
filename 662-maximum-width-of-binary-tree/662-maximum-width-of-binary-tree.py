# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        li = [(root,1)]
        
        while len(li) > 0:
            result = max(result,li[-1][1]-li[0][1]+1)
            
            new_list = []
            for value in li:
                node = value[0]
                size = value[1]
                
                if node and node.left:
                    new_list.append((node.left,size*2))
                
                if node and node.right:
                    new_list.append((node.right,size*2+1))
            
            
            li = new_list

        return result
                
            
            