# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        steps = 1
        res = None

        def visit(node):
            nonlocal steps, res
            if not node or res is not None:
                return

            visit(node.left)
            if steps == k:
                res = node.val
            steps += 1
            visit(node.right)

        visit(root)
        return res
