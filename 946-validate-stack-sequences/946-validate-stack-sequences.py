class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        queue, popIndex = collections.deque(), 0
        for i in pushed:
            queue.append(i)
            while len(queue) > 0 and popIndex < len(popped):
                if queue[-1] == popped[popIndex]:
                    queue.pop()
                    popIndex+=1
                else:
                    break
        
        if popIndex >= len(popped) and len(queue) == 0:
            return True
        
        return False