# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0)])
        result = []

        while q:
            current, depth = q.popleft()
            if not current:
                continue

            if len(result) < depth + 1:
                result.append([])
            result[depth].append(current.val)

            q.append((current.left, depth + 1))
            q.append((current.right, depth + 1))

        return result

