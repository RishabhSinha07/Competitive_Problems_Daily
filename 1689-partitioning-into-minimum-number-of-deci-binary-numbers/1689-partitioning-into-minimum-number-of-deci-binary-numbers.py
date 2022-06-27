class Solution:
    def minPartitions(self, n: str) -> int:
        """
        32
        
        1 + 1 + 1 = 3
        1 + 1 + 0 = 2
        
        11+11+10 = 32
        
        
        82734
        
        8 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
        2 = 1 + 1 + 0 + 0 + 0 + 0 + 0 + 0
        7 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 0
        3 = 1 + 1 + 1 + 0 + 0 + 0 + 0 + 0
        4 = 1 + 1 + 1 + 1 + 0 + 0 + 0 + 0
        
        11111
        11111
        10111
        10101
        10100
        10100
        10100
        10000
        -----
        82734
        
        Each number can be sum of 1's. Therefore we can check the max number of values required for any single number and return
        """
        
        res = 0
        for i in n:
            res = max(res, int(i))
        
        return res