class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # p1 and p2 at start
        # we will move p2 untill discc
        # we add p1->p2-1 to the result
        # we move p1 to p2, continue
        # Interst the left over
        
        p1, p2, res = 0, 0, []
        while p2 < len(nums):
            if p2!=len(nums)-1 and nums[p2]==nums[p2+1]-1:
                p2+=1
            else:
                if p2==p1:
                    res.append(str(nums[p1]))
                    p2+=1
                    p1+=1
                else:
                    res.append(str(nums[p1])+'->'+str(nums[p2]))
                    p2+=1
                    p1=p2
        return res