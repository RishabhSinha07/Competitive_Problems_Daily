class Solution:
    def merge(self,l1,l2):
        res = []
        
        l,r = 0,0
        while l<len(l1) and r<len(l2):
            if l1[l]<=l2[r]:
                res.append(l1[l])
                l+=1
            else:
                res.append(l2[r])
                r+=1
        
        if l < len(l1):
            res+=l1[l:]
        if r < len(l2):
            res+=l2[r:]
        
        return res
        
    def sortColors(self, nums: List[int]) -> None:
        if len(nums)==1:
            return nums
        mid = len(nums)//2
        l,r = self.sortColors(nums[:mid]),self.sortColors(nums[mid:])
        temp = self.merge(l,r)
        for i in range(len(nums)):
            nums[i]=temp[i]
        return nums
        
            
            