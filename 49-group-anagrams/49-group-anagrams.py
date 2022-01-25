class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = collections.defaultdict(list)
        
        for i in strs:
            j = ''.join(sorted(i))
            data[j].append(i)
        
        
        return data.values()
        