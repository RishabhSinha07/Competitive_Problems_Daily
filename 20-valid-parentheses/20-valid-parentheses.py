class Solution:
    def isValid(self, s: str) -> bool:
        data = {'}' : '{',')' : '(',']' : '['}
        temp = []
        
        for i in s:
            if i in ['(','[','{']:
                temp.append(i)
            else:
                if len(temp) == 0 or data[i] != temp[-1]:
                    return False
                else:
                    temp.pop()
        if len(temp) != 0: return False
        return True