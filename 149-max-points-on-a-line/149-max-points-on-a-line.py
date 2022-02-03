class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(x1,y1,x2,y2):
            if x2-x1==0:
                return 'inf'
            if y2-y1==0:
                return 'xinf'
            return (y2-y1)/(x2-x1)
        
        res = 0
        for i in range(len(points)):
            slopes = collections.defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    slopes[slope(points[i][0],points[i][1],points[j][0],points[j][1])]+=1
            if len(slopes) > 0:
                res = max(res, max(slopes.values()))
        
        return res+1