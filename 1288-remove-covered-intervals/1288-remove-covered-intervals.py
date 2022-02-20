class Solution:
    def sol1(self,intervals):
        # O(n^2) Time complexity
        res = []
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                a = intervals[i]
                b = intervals[j]
                if i != j and b[0]<=a[0] and a[1]<=b[1]:    
                    res.append((tuple(intervals[i])))
                    break
        
        res = list(set(res))
        return len(intervals)-len(res)
    
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # O(nlogn) Time Complexity
        intervals.sort(key = lambda x : x[0])
        result = 0
        cl, cr = intervals[0][0], intervals[0][1]
        
        for i in range(1,len(intervals)):
            left, right = intervals[i][0], intervals[i][1]
            
            if (left == cl and right == cr) or (cl <= left and right <= cr):
                result+=1
                continue
            
            if left <= cl and cr <= right:
                result+=1
            
            cl = left
            cr = right
                
        
        return len(intervals)-result