class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord is None or endWord is None or len(wordList) == 0:
            return 0
        if endWord not in wordList:
            return 0
        
        N ,res = len(beginWord), float('inf')
        visited = collections.defaultdict(bool)
        data = collections.defaultdict(list) 
        queue = collections.deque()
        
        for word in wordList:
            for i in range(N):
                data[word[:i]+'*'+word[i+1:]].append(word)
        
        queue.append((beginWord,0))
        while queue:
            curr, depth = queue.popleft()
            if visited[curr]:
                continue
            visited[curr] = True
            if curr == endWord:
                res=min(res,depth)
                continue
            for i in range(N):
                for j in data[curr[:i]+'*'+curr[i+1:]]:
                    queue.append((j,depth+1))
        
        if res > len(wordList)+1:
            return 0
        return res+1
                