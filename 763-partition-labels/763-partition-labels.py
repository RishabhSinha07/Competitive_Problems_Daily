class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        data = {}
        for i,j in enumerate(s):
            data[j]=i
        
        max_index, result, size = 0, [], 0
        for i,j in enumerate(s):
            size+=1
            max_index = max(max_index,data[j])
            if max_index == i:
                result.append(size)
                size=0
        return result