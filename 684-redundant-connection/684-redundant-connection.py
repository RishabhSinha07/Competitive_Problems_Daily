class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        
        
        def find(node):
            nonlocal parent
            p = parent
            if p[node] == node:
                return node
            while p[node] != node:
                p[node] = p[p[node]]
                node = p[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            nonlocal rank
            nonlocal parent
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2]+=rank[p1]
            return 1
        
        ri,rj = -1,-1
        for i,j in edges:
            temp = union(i,j)
            if temp == 0:
                ri,rj = i,j
        
        return [ri,rj]
        