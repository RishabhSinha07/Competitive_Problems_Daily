class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Union Find Approch
        cities = len(isConnected)
        parent, count = [i for i in range(cities)], [1]*cities
        
        def find(city):
            nonlocal parent
            while parent[city] != city:
                parent[city] = parent[parent[city]] # Path compression
                city = parent[city]    
            return city
        
        def union(city1, city2):
            nonlocal count
            p1, p2 = find(city1), find(city2)
            
            if p1 == p2:
                return 0
            
            if count[p1] >= count[p2]:
                parent[p2] = p1
                count[p1] += count[p2]
            else:
                parent[p1] = p2
                count[p2] += count[p1]
            
            return 1
        
        result = cities
        for i in range(cities):
            for j in range(cities):
                if isConnected[i][j] == 1:
                    result-=union(i,j)
                    
        return result