class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result1, value1, value2 = 0, tops[0], bottoms[0]
        
        score1, score2, flag1, flag2 = 0, 0, True, True
        for i,j in zip(tops,bottoms):
            if not flag1 and not flag2:
                return -1
            if flag1 and value1 != i and value1 !=j:
                flag1=False
            if flag2 and value2 != i and value2 !=j:
                flag2=False
            
            if flag1 and i != value1 and j==value1:
                score1+=1
            if flag2 and i != value2 and j==value2:
                score2+=1
        if not flag1 and not flag2:
            result1 = -1
        if flag1 and not flag2:
            result1 = score1
        if flag2 and not flag1:
            result1 = score2
        if flag1 and flag2:
            result1 = min(score1,score2)
        
        tops, bottoms = bottoms, tops
        result2, value1, value2 = 0, tops[0], bottoms[0]
        
        score1, score2, flag1, flag2 = 0, 0, True, True
        for i,j in zip(tops,bottoms):
            if not flag1 and not flag2:
                return -1
            if flag1 and value1 != i and value1 !=j:
                flag1=False
            if flag2 and value2 != i and value2 !=j:
                flag2=False
            
            if flag1 and i != value1 and j==value1:
                score1+=1
            if flag2 and i != value2 and j==value2:
                score2+=1
        if not flag1 and not flag2:
            result2 = -1
        if flag1 and not flag2:
            result2 = score1
        if flag2 and not flag1:
            result2 = score2
        if flag1 and flag2:
            result2 = min(score1,score2)
        
        if result1 != 0 and result2 != 0:
            return min(result1,result2)
        if result1 == 0:
            return result2
        return result1
        