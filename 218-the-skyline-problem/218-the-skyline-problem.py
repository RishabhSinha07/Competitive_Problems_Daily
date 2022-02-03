class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Sweep Line Algorithm. 
        edges = set()
        sweep = collections.defaultdict(list)
        
        for start, end, height in buildings:
            edges.add(start)
            edges.add(end)
            
            # 1 stands for start and -1 for end
            sweep[start].append((1,height))
            sweep[end].append((-1,height))
        
        result = []
        
        temp = [0]
        for pos in sorted(list(edges)):
            for status, height in sweep[pos]:
                if status == 1:
                    temp.append(height)
                else:
                    temp.remove(height)
            if len(result) == 0 or max(temp)!=result[-1][1]:
                result.append([pos,max(temp)])
        
        return result
                
            
            