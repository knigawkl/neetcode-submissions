from typing import List

class Solution:
    def is_valid(self, matrix, r, c, visited):
        R, C = len(matrix), len(matrix[0])
        return 0 <= r < R and 0 <= c < C and not visited[r][c]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        R, C = len(matrix), len(matrix[0])
        visited = [[False] * C for _ in range(R)]
        r, c = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        curr_dir = 0
        result = []

        while len(result) < R * C:
            result.append(matrix[r][c])
            visited[r][c] = True

            # try to keep going in current direction
            nr = r + directions[curr_dir][0]
            nc = c + directions[curr_dir][1]

            # if cannot go further, turn right (spiral behavior)
            if not self.is_valid(matrix, nr, nc, visited):
                curr_dir = (curr_dir + 1) % 4
                nr = r + directions[curr_dir][0]
                nc = c + directions[curr_dir][1]

            r, c = nr, nc

        return result