import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def validNode(self, node, l, r):
        if not node:
            return True

        if node.val > l and node.val < r:
            return self.validNode(node.left, l, node.val) and self.validNode(node.right, node.val, r)

        return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if self.validNode(root, -math.inf, math.inf):
            return True
