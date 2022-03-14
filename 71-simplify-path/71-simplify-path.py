class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [x for x in path.split('/') if x not in ['.','']]
        
        prev_actual_dir_index = collections.deque()
        for i in range(len(path)):
            dots = path[i].count('.')
            if dots == 0 or dots != len(path[i]):
                prev_actual_dir_index.append(i)
                continue
            if dots == 2:
                path[i] == ""
                if prev_actual_dir_index:
                    path[prev_actual_dir_index.pop()] = ""

        
        return '/'+'/'.join([x for x in path if x not in ['','..']])
                
                
        