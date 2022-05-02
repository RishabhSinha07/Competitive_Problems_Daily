class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        res = []
        for i in even:
            res.append(i)
        for i in odd:
            res.append(i)
        return res