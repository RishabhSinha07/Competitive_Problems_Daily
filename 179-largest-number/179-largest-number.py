class Solution:
    def compare(self,l1,l2):
        # 1 : l1 > l2 and 0 : l2 >= l1
        return str(l1)+str(l2)>str(l2)+str(l1)
    
    def merge(self, left, right):
        result = []
        l, r = 0, 0
        
        while l < len(left) and r < len(right):
            if self.compare(left[l],right[r]):
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
        if l < len(left):
            result+=left[l:]
        if r < len(right):
            result+=right[r:]
        
        return result
    
    def mergeSort(self,arr,l,r):
        if l >= r:
            return [arr[l]]
        
        mid = l+(r-l)//2
        
        left = self.mergeSort(arr,l,mid)
        right = self.mergeSort(arr,mid+1,r)
        
        return self.merge(left,right)
    
    def largestNumber(self, nums: List[int]) -> str:
        nums = self.mergeSort(nums,0,len(nums)-1)
        nums = [str(x) for x in nums]
        return str(int("".join(nums)))