class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans=[]
        count1=0
        for i in nums:
            if i==1:
                count1+=1
        count0=0
        max_score=0
        n=len(nums)
        for i in range(0,n+1):
            temp=count0+count1
            if temp>max_score:
                ans=[i]
                max_score=temp
            elif temp==max_score:
                ans.append(i)
            if i<n:
                if nums[i]==0:
                    count0+=1
                else:
                    count1-=1
        return ans
        
        
        
        
        
        
        '''
        # 6000 ms solution
        N = len(nums)
        values = [0]*(N+1)
        
        count = 0
        for i in range(N):
            values[i]=count
            if nums[i] == 0:count+=1
        values[-1] = count
        
        count = 0
        for i in range(N-1,-1,-1):
            count+=nums[i]
            values[i] += count
        
        max_value = max(values)
        return [x for x in range(N+1) if values[x] == max_value]

        '''
        
        