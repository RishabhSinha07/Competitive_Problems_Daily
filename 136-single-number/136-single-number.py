from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for val in nums:
            d[val]+=1
        for i in d.keys():
            if d[i] == 1:
                return i