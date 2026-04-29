class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # counting connected components
        R, C = len(grid), len(grid[0])

        def dfs(grid, visited, start_r, start_c):
            def is_valid(r, c):
                return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and not (r, c) in visited and grid[r][c] == "1"

            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            visited.add((start_r, start_c))
            def visit(r, c):
                for dir_r, dir_c in directions:
                    nbr_r, nbr_c = r + dir_r, c + dir_c
                    if is_valid(nbr_r, nbr_c):
                        visited.add((nbr_r, nbr_c))
                        visit(nbr_r, nbr_c)
            visit(start_r, start_c)

        count = 0
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    dfs(grid, visited, r, c)
                    count += 1
        return count

    
