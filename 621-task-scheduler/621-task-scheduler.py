import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        data, track = [], collections.Counter(tasks)
        for i,v in track.items():
            heappush(data,[-v,i])
        
        current_time = 0
        processed = deque()
            
        while len(data) > 0 or len(processed) > 0:
            current_time+=1
            if len(data) > 0:
                current = heappop(data)
                current[0]+=1
                if current[0] < 0:
                    processed.append([current,current_time+n])
            if len(processed) > 0 and processed[0][1] <= current_time:
                value = processed.popleft()
                heappush(data,value[0])
        return current_time