class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        
        def dfs(li,index):
            if len(li) == 4:
                if index == len(s):
                    self.result.append('.'.join(li))
                return
            
            
            for i in range(index,index+3):
                if i < len(s):
                    if index!=i and s[index]=='0':
                        continue
                    if 0<=int(s[index:i+1])<=255:
                        dfs(li+[s[index:i+1]],i+1)
                else:
                    break
        
        dfs([],0)
        return self.result
                    