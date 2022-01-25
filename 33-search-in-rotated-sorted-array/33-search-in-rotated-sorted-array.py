class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        What do we know ?
        1. array was sorted initially
        2. It was rotated counter clockwise
        
        we need to use binary search for this operation to get O(logn) TC. 
        The question is how to choose which side we want to go? 
        
        For this purpose we can track the at most left and  right value of the array.
        And whenever we get mid we can check if target is present b/w the value nums[left] to nums[mid] or
        nums[mid] to nums[right]. And based on that we can choose the path for BS.
        
        '''
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            
            if nums[left] < nums[mid]:
                if nums[left]<target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target<nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        
        
        return -1
            
                
        