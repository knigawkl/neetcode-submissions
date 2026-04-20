# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def visit(node, depth):
            nonlocal res
            if not node:
                return 0
            left_depth = visit(node.left, depth + 1)
            right_depth = visit(node.right, depth + 1)
            current_depth = 1 + max(left_depth, right_depth)
            res = max(res, current_depth)
            return current_depth

        visit(root, 0)
        return res
