class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i != j:
                    a = intervals[i]
                    b = intervals[j]
                    if b[0]<=a[0] and a[1]<=b[1]:
                        res.append((tuple(intervals[i])))
                        break
        
        res = list(set(res))
        return len(intervals)-len(res)
                    