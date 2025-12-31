class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        T_matrix = [[0]*rows for _cols in matrix[0]]

        for i in range(cols):
            for j in range(rows):
                T_matrix[i][j] = matrix[j][i]
        return T_matrix