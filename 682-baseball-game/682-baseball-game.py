class Solution:
    def calPoints(self, ops: List[str]) -> int:
        li = collections.deque()
        
        for value in ops:
            if value == '+':
                li.append(li[-1]+li[-2])
            elif value == 'D':
                li.append(li[-1]*2)
            elif value == 'C':
                li.pop()
            else:
                li.append(int(value))
        return sum(li)