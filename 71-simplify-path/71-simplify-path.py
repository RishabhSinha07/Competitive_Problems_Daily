class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [x for x in path.split('/') if x not in ['.','']]
        
        for i in range(len(path)):
            dots = path[i].count('.')
            if dots == 1 and len(path[i]) == 2:
                path[i]=''
            if dots == 2 and len(path[i]) == 2:
                path[i]=''
                temp = i
                while temp>=0 and path[temp]=='':
                    temp-=1
                if temp >= 0:
                    path[temp]=''
        
        path = [x for x in path if x != '']
        path = '/'.join(path)
        return "/"+path
                
                
        