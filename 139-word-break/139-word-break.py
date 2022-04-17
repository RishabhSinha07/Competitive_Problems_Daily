class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(word):
            if word in wordDict:
                return True
            temp1 = ""
            for index, char in enumerate(word):
                temp1+=char
                if temp1 in wordDict and dfs(word[index+1:]):
                    return True
                
                
        return dfs(s)