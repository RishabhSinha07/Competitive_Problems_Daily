class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        
        bit = [0 for _ in range(N)]
        lgt = [0 for _ in range(N)]
        
        for i in range(N):
            for j in range(len(words[i])):
                bit[i]|=1<<(ord(words[i][j]) - ord('a'))
            lgt[i] = len(words[i])
        
#         print(bit)
#         print(lgt)
        
        res = 0
        
        for i in range(N):
            for j in range(i,N):
                if not bit[i]&bit[j]:
                    res = max(res, lgt[i]*lgt[j])
        
        return res