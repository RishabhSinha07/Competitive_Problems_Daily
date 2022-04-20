# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push(root)
        
    def push(self, node):
        if node is None:
            return
        self.stack.append(node)
        self.push(node.left)

    def next(self) -> int:
        temp = self.stack.pop(-1)
        self.push(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()