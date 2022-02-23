"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = {}
        
        def fn(node):
            if node is None:return None
        
            nNode = Node(node.val)
            self.visited[node] = nNode
            for i in node.neighbors:
                if i not in self.visited:
                    self.visited[i] = fn(i)
                nNode.neighbors.append(self.visited[i])

            return nNode
        
        return fn(node)