class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)
        res = high
        def help(value):
            a,b = 0,0
            for i in nums:
                b+=i
                if b>value:
                    a+=1
                    b=i
            return a+1 <= m
        
        while low <= high:
            mid = low + (high-low)//2
            if help(mid):
                res = mid
                high = mid-1
            else:
                low = mid+1
        
        return res