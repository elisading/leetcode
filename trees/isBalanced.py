# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node):
        if not node:
            return -1
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_h = self.height(root.left)
        right_h = self.height(root.right)

        if abs(left_h - right_h) > 1:
            return False

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
