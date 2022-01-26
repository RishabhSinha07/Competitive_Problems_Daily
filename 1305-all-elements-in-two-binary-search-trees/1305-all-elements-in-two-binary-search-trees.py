# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        '''
        Do inorder traversal for both the trees. 
        Iterate through the lists and then create a new list with
        sorted array in linear time. 
        
        [a,b,c,d]
        [e,f,g,f]
        
        [].append(a) if a<=e and a+=1 so on...
        
        '''
        
        def dfs(root,res):
            if root is None:
                return []
            dfs(root.left,res)
            res+=[root.val]
            dfs(root.right,res)
            return res
        
        a = dfs(root1,[])
        b = dfs(root2,[])
#         if len(a) == 0:
#             return b
        
#         if len(b) == 0:
#             return a
        
        res = []
        
        ai = bi = 0
        while ai < len(a) and bi < len(b):
            if a[ai]<=b[bi]:
                res.append(a[ai])
                ai+=1
            else:
                res.append(b[bi])
                bi+=1
        
        if ai < len(a):
            for i in range(ai,len(a)):
                res.append(a[i])
        
        if bi < len(b):
            for i in range(bi,len(b)):
                res.append(b[i])
        
        return res
        