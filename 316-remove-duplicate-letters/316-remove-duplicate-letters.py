class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # We want to keep the elements ordered
        # If the element is the last element of a particulat type we don't care about the order
        
        order = collections.defaultdict(int)
        for i,j in enumerate(s):
            order[j]=i
        
        counter = collections.defaultdict(int)
        for i in s:
            counter[i]=1
            
        pq = collections.deque([])
        
        for index, c in enumerate(s):
            if counter[c] <= 0:
                continue
            if len(pq) == 0:
                pq.append(c)
                counter[c]-=1
            else:
                if pq[-1] > c:
                    # Remove the value untill its the pq is enpty, value is less then c or its the last elment in the list
                    while len(pq) > 0 and pq[-1] > c and order[pq[-1]] > index:
                        temp = pq.pop()
                        counter[temp]+=1
                pq.append(c)
                counter[c]-=1
        return ''.join(pq)