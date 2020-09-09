# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root, li):
        if not root:
            return
        self.traversal(root.left, li)
        li.append(root.val)
        self.traversal(root.right, li)
        return li

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.traversal(root, [])


# Runtime: 32 ms, faster than 63.16% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.9 MB, less than 32.92% of Python3 online submissions for Binary Tree Inorder Traversal.
