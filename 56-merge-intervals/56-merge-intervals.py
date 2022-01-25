class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        
        result = []

        for cx,cy in intervals:
            
            if len(result) == 0:
                result.append([cx,cy])
                continue
            
            ox,oy = result[-1]
            
            if ox <= cx <= oy and cy >= oy:
                result.pop(-1)
                result.append([ox,cy])
            elif ox <= cx <= oy and cy < oy:
                continue
            else:
                result.append([cx,cy])
        
        return result
                