class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, value):
        temp = self.node
        for i in range(len(value)):
            if value[i] not in temp.child:
                temp.child[value[i]] = TrieNode()
            temp = temp.child[value[i]]
        temp.end = True

    def check(self,value):
        org = value
        value = bin(1<<33|value)[3:]
        temp, res = self.node, []
        for i in range(len(value)):
            if value[i]=='1':
                if '0' in temp.child:
                    res.append('0')
                    temp = temp.child['0']
                else:
                    res.append('1')
                    temp = temp.child['1']
            else:
                if '1' in temp.child:
                    res.append('1')
                    temp = temp.child['1']
                else:
                    res.append('0')
                    temp = temp.child['0']
                    
        return int(''.join(res),2)^org



class Solution:    
    def findMaximumXOR(self, nums: List[int]) -> int:
        t = Trie()
        res = 0
        for i in nums:
            t.insert(bin(1<<33|i)[3:])
        
        for i in nums:
            res = max(res, t.check(i))
        
        return res