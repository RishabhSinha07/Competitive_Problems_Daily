# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, res = [[root]], []
        
        while len(q) > 0:
            curr = q.pop(0)
            temp, newq = [], []
            for node in curr:
                if node:
                    temp.append(node.val)
                    newq.append(node.left)
                    newq.append(node.right)
            if len(newq)>0:
                res.append(temp)
                q.append(newq)
        
        return res
                    