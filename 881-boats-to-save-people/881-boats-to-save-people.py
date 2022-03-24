class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        data = sorted(people)
        start, boats = 0, 0
        end = len(data)-1
        
        for start in range(len(data)):
            if data[start] == 'X':
                continue
            req_weight = limit - data[start]
            while end > 0 and (data[end] == 'X' or data[end] > req_weight):
                end-=1
            if data[end] != 'X' and data[end] <= req_weight:
                data[end] = 'X'
            boats+=1
        
        
        return boats
        