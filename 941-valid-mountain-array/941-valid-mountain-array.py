class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        '''
        First set of values should increase always and 
        whenever we find a value lesser than the current
        from then it should decrease. 
        '''
        if len(arr)<3:
            return False
        
        inc = True
        
        for i in range(1,len(arr)-1):
            if arr[i]==arr[i+1] or arr[i] == arr[i-1]:
                return False
            elif arr[i-1]<arr[i]>arr[i+1] and inc:
                inc = False
            elif not arr[i-1]<arr[i]<arr[i+1] and inc:
                return False
            elif not arr[i-1]>arr[i]>arr[i+1] and not inc:
                return False
        
        return not inc
            