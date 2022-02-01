"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        q = collections.deque()
        q.append([root])
        
        while q:
            current = q.popleft()
            current[-1].next = None
            
            new = []
            for i in range(len(current)):
                if i < len(current) -1 :
                    current[i].next = current[i+1]
                if current[i].left:
                    new.append(current[i].left)
                if current[i].right:
                    new.append(current[i].right)
                
            if len(new) > 0:
                q.append(new)
            
            
        return root