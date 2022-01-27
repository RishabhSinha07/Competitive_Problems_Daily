class Solution:
    def dfs(self, x, y, m, count, word):
        if count == len(word):
            return True
        if x<0 or x>=len(m) or y<0 or y>=len(m[0]) or m[x][y] != word[count]:
            return False
        temp = m[x][y]
        m[x][y] = ''
        if self.dfs(x+1,y,m,count+1,word) or self.dfs(x-1,y,m,count+1,word) or self.dfs(x,y+1,m,count+1,word) or self.dfs(x,y-1,m,count+1,word):
            return True
        m[x][y] = temp
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(i,j,board,0,word):
                    return True
        return False