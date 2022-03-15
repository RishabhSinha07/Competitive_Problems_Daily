class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s= list(s)
        data = []
        remove = []
        
        for i,j in enumerate(s):
            if j == '(':
                data.append([i,j])
                continue
            if j == ')':
                if len(data) > 0 and data[-1][1] == '(':
                    data.pop(-1)
                else:
                    remove.append(i)
        
        for i in data:
            remove.append(i[0])
        
        for i in remove:
            s[i] = ""
            
        return ''.join(s)