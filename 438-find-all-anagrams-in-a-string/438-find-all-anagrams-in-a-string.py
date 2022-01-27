class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        q = collections.deque()
        r = collections.Counter(p)
        
        res = []
        temp = collections.defaultdict(int)
        for index, i in enumerate(s):
            if r[i] == 0:
                while q: 
                    val=q.popleft()
                    temp[val]-=1
                continue
                    
            q.append(i)
            temp[i]+=1
            if len(q) == len(p):
                if temp == r:
                    res.append(index-len(p)+1)
                val = q.popleft()
                temp[val]-=1
        
        return res