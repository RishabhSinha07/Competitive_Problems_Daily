# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.li = []
        self.iot(root)
        self.pos = 0
        
    def iot(self, node):
        if node is None:
            return
        self.iot(node.left)
        self.li.append(node.val)
        self.iot(node.right)
    
    def next(self) -> int:
        self.pos+=1
        return self.li[self.pos-1]

    def hasNext(self) -> bool:
        if self.pos < len(self.li):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()