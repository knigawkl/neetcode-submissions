class Solution:
    def transpose(self, matrix):
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        return matrix
    
    def reflect_horizontally(self, matrix):
        for row in matrix:
            row.reverse()
    
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        self.transpose(matrix)
        self.reflect_horizontally(matrix)
    