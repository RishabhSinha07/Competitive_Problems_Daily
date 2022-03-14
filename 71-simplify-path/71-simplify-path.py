class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [x for x in path.split('/') if x not in ['.','']]
        
        for i in range(len(path)):
            dots = path[i].count('.')
            if dots == 0 or dots != len(path[i]):
                continue
            if dots == 2:
                path[i], temp = '', i
                while temp>=0 and path[temp]=='':
                    temp-=1
                if temp >= 0: path[temp]=''
        
        return '/'+'/'.join([x for x in path if x != ''])
                
                
        