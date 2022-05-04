class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        data, count = collections.defaultdict(int), 0
        for i in nums:
            if i in data and data[i]>0:
                count+=1
                data[i]-=1
            else:
                data[k-i]+=1
        return count
                