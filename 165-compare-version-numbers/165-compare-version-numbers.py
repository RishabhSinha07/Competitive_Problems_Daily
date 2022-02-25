class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        length = max(len(version1),len(version2))
        
        v1, v2 = [], []
        
        for i in range(length):
            if i < len(version1) and version1[i].lstrip('0')!='':
                v1.append(version1[i].lstrip('0'))
            else:
                v1.append('0')
            
            if i < len(version2) and version2[i].lstrip('0') != '':
                v2.append(version2[i].lstrip('0'))
            else:
                v2.append('0')
        
        
        v1 = int(''.join(v1))
        v2 = int(''.join(v2))
        
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0
        
        
        
        
        