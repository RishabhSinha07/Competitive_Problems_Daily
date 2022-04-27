class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        parent, rank = [i for i in range(N)], [1 for _ in range(N)]
        
        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]] # optimization
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # If they are already grouped together
            if p1 == p2:
                return 0
            # If they are not:
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1]+=1
            else:
                parent[p1] = p2
                rank[p2]+=1
            return 1
        
        # Run union find
        for i,j in pairs:
            union(i,j)
        
        # Create data
        data = collections.defaultdict(list)
        for i,j in enumerate(s):
            p = find(i)
            data[p].append([i,j])
        
        # Creating result
        res = ['' for _ in range(N)]
        for value in data.values():
            indices = [x[0] for x in value]
            char = [x[1] for x in value]
            
            indices.sort()
            char.sort()
            
            for i,j in zip(indices, char):
                res[i]=j
        return ''.join(res)
        
            