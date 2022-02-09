class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        '''
        Brute force appx:
        
        For each element, iterate through the rest of the list
        from i+1 to end give i is the current position. Check the cond
        mod(nums[i]-nums[i+x]) == res and add to a set for unique ans.
        
        TC : O(n^2)
        SC : O(1)
        
        For Faster Appx:
        
        - We can try to eliminate the searching part through the sub array. 
        - We can leverage map for that. 
        
        - What we are trying to do in BF?
        > For each current value we are trying to find if the following cond
          satisfy:
          - c-b = t : b = c-t 
          - b-c = t : b = t+c
          
          we want to see if we have (t+c) or (c-t) in the map
          
          nums = [3,1,4,1,5], k = 2
          - For 3 we want to check if (2+3 or 3-2) = (5,1) is present anywhere
            in the list. 
          ....... so on
          
          * The order does not matter here as the diff shoudl be absolute. 
       
       TC : O(N)
       SC : O(N)
     
        '''
        
        map = collections.Counter(nums)
        
        result = 0
        for i in map:
            val1 = k+i
            if (k > 0 and map[val1]>0) or (k==0 and map[val1]>1):
                result+=1
        
        
        return result