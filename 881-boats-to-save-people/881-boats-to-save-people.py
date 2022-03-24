class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        data = collections.defaultdict(int)
        for i in people:data[i]+=1
        
        boats = 0
        for i in people:
            if data[i] <= 0:
                continue
            data[i]-=1
            req_weight = limit-i
            
            while req_weight > 0:
                if data[req_weight] > 0:
                    data[req_weight]-=1
                    break
                req_weight-=1
            boats+=1
        
        return boats