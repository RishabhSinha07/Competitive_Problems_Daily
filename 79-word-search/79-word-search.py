class Solution:
    
    def dfs(self, board, i, j, count, word):
        if count == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j>= len(board[i]) or board[i][j] != word[count]:
            return False
        count+=1
        temp = board[i][j]
        board[i][j] = ' '
        found = self.dfs(board,i+1,j,count,word) or self.dfs(board,i-1,j,count,word) or                                       self.dfs(board,i,j+1,count,word) or self.dfs(board,i,j-1,count,word)
        board[i][j] = temp
        return found
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):
                    return True
        return False