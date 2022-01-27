class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        q = collections.deque()
        r = collections.Counter(p)
        
        res = []
        
        for index, i in enumerate(s):
            if r[i] == 0:
                while q: q.popleft()
                continue
                    
            q.append(i)
            if len(q) == len(p):
                temp = collections.Counter(q)
                if temp == r:
                    res.append(index-len(p)+1)
                q.popleft()
        
        return res