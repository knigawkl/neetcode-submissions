"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned = dict()
        cloned[node] = Node(node.val, [])

        q = deque([node])
        while q:
            cur = q.popleft()
            for nbr in cur.neighbors:
                if nbr not in cloned:
                    cloned[nbr] = Node(nbr.val, [])
                    q.append(nbr)
                cloned[cur].neighbors.append(cloned[nbr])
        
        return cloned[node]
