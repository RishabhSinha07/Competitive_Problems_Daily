# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    nodes = [[root]]
    final = []
    while len(nodes) > 0:
        temp = nodes.pop(0)
        z = []
        zn = []
        for i in temp:
            if i is None:
                continue
            z.append(i.val)
            zn.append(i.left)
            zn.append(i.right)
        if len(z) > 0:
            final.append(z)
        if len(zn) > 0:
            nodes.append(zn)
    return final


if __name__ == "__main__":
    print(levelOrder([3, 9, 20, None, None, 15, 7]))


# Runtime: 36 ms, faster than 72.50% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.1 MB, less than 57.28% of Python3 online submissions for Binary Tree Level Order Traversal.
