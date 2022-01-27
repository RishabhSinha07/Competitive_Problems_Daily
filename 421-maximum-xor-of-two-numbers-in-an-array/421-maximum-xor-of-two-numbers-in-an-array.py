class TrieNode:
    def __init__(self):
        self.child = {}

class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, value):
        temp = self.node
        for i in value:
            if i not in temp.child:temp.child[i] = TrieNode()
            temp = temp.child[i]

    def check(self, value):
        original_value = value
        value = bin(1<<32|value)[3:]
        
        temp, res = self.node, []
        for i in value:
            if (i=='1' and '0' in temp.child) or (i=='0' and '1' not in temp.child):
                res.append('0')
                temp = temp.child['0']
            else:
                res.append('1')
                temp = temp.child['1']
                    
        return int(''.join(res),2)^original_value



class Solution:    
    def findMaximumXOR(self, nums: List[int]) -> int:
        t = Trie()
        res = 0
        for i in nums:
            t.insert(bin(1<<32|i)[3:])
        
        for i in nums:
            res = max(res, t.check(i))
        
        return res