class Solution:
    def find(self, graph, start, end, res, visited):
        if start == end:return res
        if start in visited or start not in graph:return -1
        visited[start]=1
        for i in graph[start]:
            temp = self.find(graph, i[0], end, res*i[1], visited)
            if temp != -1: return temp   
        return -1
        
    def search(self, graph, q):
        start, end = q[0], q[1]
        if start not in graph or end not in graph: return -1
        return self.find(graph, start, end, 1, {})
    
    def calcEquation(self, equations, values, queries):
        res, aList = [], collections.defaultdict(list)
        
        for eq,val in zip(equations,values):
            aList[eq[0]].append((eq[1],val))
            aList[eq[1]].append((eq[0],1/val))
        
        for q in queries:
            res.append(self.search(aList,q))
            
        return res