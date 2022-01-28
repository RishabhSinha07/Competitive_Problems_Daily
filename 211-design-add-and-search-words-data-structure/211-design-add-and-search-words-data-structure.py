'''
Trie is the way to go for sure. 

The only thing different here is the "." mechanism which says dot matches all. 
Therefore when we are searching in the trie and we encounter '.' we need to try
all the values present in the child map of the node.

TC : 500*N where N = len(input)
'''
class Node:
    def __init__(self):
        self.child = {}
        self.end = 0

class WordDictionary:

    def __init__(self):
        self.node = Node()

    def addWord(self, word: str) -> None:
        temp = self.node
        for char in word:
            if char not in temp.child:
                temp.child[char] = Node()
            temp = temp.child[char]
        temp.end = 1

    def search(self, word: str) -> bool:
        temp = self.node
        
        def dfs(node, pos, word):
            if pos >= len(word):
                if node.end == 1:
                    return True
                else:
                    return False
            if word[pos] != '.' and word[pos] not in node.child:
                return False
            if word[pos] == '.':
                for child_value in node.child:
                    if dfs(node.child[child_value],pos+1, word):
                        return True
            else:
                return dfs(node.child[word[pos]],pos+1, word)

        
        return dfs(temp, 0, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)