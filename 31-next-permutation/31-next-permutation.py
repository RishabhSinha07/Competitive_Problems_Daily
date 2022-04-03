class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        refpoint = None
        
        for index in range(len(nums)-1,0,-1):
            if nums[index-1]<nums[index]:
                refpoint = index-1
                break
        temp = []
        if refpoint is not None:
            for index in range(len(nums)-1,-1,-1):
                if nums[index] > nums[refpoint]:
                    nums[index],nums[refpoint] = nums[refpoint],nums[index]
                    temp = nums[:refpoint+1] + sorted(nums[refpoint+1:])
                    break
            for i,j in enumerate(temp):
                nums[i]=j
        else:
            nums.reverse()
    