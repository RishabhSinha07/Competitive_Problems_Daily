class Solution:
    def fib(self, n: int) -> int:
        series = [0,1]
        for i in range(2,n+1):
            series.append(series[i-1]+series[i-2])
        
        return series[n]
            