# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        Complete Bianry Tree : All the nodes should have left and right nodes except the last and
        second last level. 
        
        The second last level should have all the left side filled before right can be filled
        The last should have all the left and right node as null

        """
        D, level = 1, collections.deque([[root]])
        while level:
            current = level.popleft()
            
            if len(current) != D:
                return False
            
            temp = []
            for node in current:
                if node:
                    temp.append(node.left)
                    temp.append(node.right)
            
            D = D*2
            if len(temp) == 0:continue
                
            tag = False
            for node in temp:
                if node and tag:return False
                if node is None:tag = True
            # End of tree
            if current[0].left is None and current[0].right is None:
                break
            level.append(temp)
        
        return True