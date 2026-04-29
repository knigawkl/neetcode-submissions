from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1

        components = 0

        graph = {node: [] for node in range(n)}
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()
        def dfs(node):
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr)

        for node in graph:
            if node in visited:
                continue
            else:
                visited.add(node)
                components += 1
                dfs(node)

        return components
