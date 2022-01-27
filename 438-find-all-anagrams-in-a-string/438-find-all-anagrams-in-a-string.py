class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Variable for result and tracking substing value freq
        res, tracker = [], collections.defaultdict(int)
        # Queue and map
        q, testcase = collections.deque(), collections.Counter(p)
        
        
        for index, char in enumerate(s):
            if testcase[char] == 0:
                while q: tracker[q.popleft()]-=1
                continue
                    
            q.append(char)
            tracker[char]+=1
            
            if len(q) == len(p):
                if tracker == testcase:
                    res.append(index-len(p)+1)
                
                tracker[q.popleft()]-=1
        
        return res