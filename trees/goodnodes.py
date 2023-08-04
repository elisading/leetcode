# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isGood(self, node, max_val, count):
        if not node:
            return count

        if node.val >= max_val:
            count += 1
            max_val = node.val

        count = self.isGood(node.left, max_val, count)
        count = self.isGood(node.right, max_val, count)

        return count

    def goodNodes(self, root: TreeNode) -> int:
        # max_val = root.val
        # count = 0

        return self.isGood(root, root.val, 0)
