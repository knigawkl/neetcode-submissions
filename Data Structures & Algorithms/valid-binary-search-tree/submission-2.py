# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(tree, low=float('-inf'), high=float('inf')):
            if not tree:
                return True
            elif not low < tree.val < high:
                return False
            is_left = is_valid(tree.left, low, tree.val)
            is_right = is_valid(tree.right, tree.val, high)
            return is_left and is_right
        return is_valid(root)
