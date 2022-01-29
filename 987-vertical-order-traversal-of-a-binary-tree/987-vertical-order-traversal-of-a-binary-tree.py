# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        tracker = collections.defaultdict(list)
        def dfs(x,y,node):
            if node is None:
                return
            tracker[(x,y)].append(node.val)
            dfs(x-1,y+1,node.left)
            dfs(x+1,y+1,node.right)
        dfs(0,0,root)
        result, visited = [], []
        for key,value in sorted(tracker.items()):
            if key[0] not in visited:
                visited.append(key[0])
                result.append([])
            result[-1].extend(sorted(value))
        
        return result
        
        
            