class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        visited = set()

        def is_valid(r, c, i):
            return 0 <= r < R and 0 <= c < C and not (r, c) in visited and word[i] == board[r][c]

        def visit(r, c, i):
            if i == len(word):
                return True
            if not is_valid(r, c, i):
                return False

            visited.add((r, c))

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            result = any(visit(r + dir_r, c + dir_c, i + 1) for dir_r, dir_c in directions)
            visited.remove((r, c))
            return result

        for r in range(R):
            for c in range(C):
                if visit(r, c, 0):
                    return True

        return False