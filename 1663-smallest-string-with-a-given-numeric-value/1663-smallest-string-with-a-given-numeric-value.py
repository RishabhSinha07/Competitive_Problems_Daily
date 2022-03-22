class Solution:
    def getScore(self, li):
        score = 0
        for i in li:
            score+=(ord(i)-96)
        return score
    
    def getSmallestString(self, n: int, k: int) -> str:
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        values = ['a']*n
        current_score = self.getScore(values)
        
        if current_score > k:
            return -1
        
        for i in range(len(values)-1,-1,-1):
            if current_score == k:
                return "".join(values)
            index = 0
            if k-current_score > 26:
                current_score-=(ord(values[i])-96)
                values[i]=alpha[-1]
                current_score+=(ord(values[i])-96)
            else:
                while current_score < k and index < 26:
                    current_score-=(ord(values[i])-96)
                    values[i]=alpha[index]
                    current_score+=(ord(values[i])-96)
                    index+=1
        
        return "".join(values)