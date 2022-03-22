class Solution:
    def alphaValue(self, alpha):
        return ord(alpha)-96
    
    def getSmallestString(self, n: int, k: int) -> str:
        Lalpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        result = ['a']*n
        current_score = n
        
        for i in range(len(result)-1,-1,-1):
            if current_score == k:
                return "".join(result)
            
            if k-current_score > 26:
                current_score-=self.alphaValue(result[i])
                result[i]=Lalpha[-1]
                current_score+=self.alphaValue(result[i])
            else:
                index = 0
                while current_score < k and index < 26:
                    current_score-=self.alphaValue(result[i])
                    result[i]=Lalpha[index]
                    current_score+=self.alphaValue(result[i])
                    index+=1
        
        return "".join(result)