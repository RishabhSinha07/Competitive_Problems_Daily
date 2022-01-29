# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        for value in nestedList:
            if value.isInteger():
                self.res.append(value.getInteger())
                continue
            self.res+=self.dfs(value)
    
    def dfs(self, node):
        if node.isInteger():return node.getInteger()
        res = []
        for x in node.getList():
            if x.isInteger():
                res.append(x.getInteger())
                continue
            res+=self.dfs(x)
        return res

    
    def next(self) -> int:
        return self.res.pop(0)
    
    def hasNext(self) -> bool:
         return len(self.res) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())