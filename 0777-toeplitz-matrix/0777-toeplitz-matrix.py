class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        rows  = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            row = i
            col = 0
            holdM = matrix[row][col]
            while row < rows-1 and col < cols-1:
                row += 1
                col += 1
                if holdM != matrix[row][col]:
                    return False
                holdM = matrix[row][col]
        for j in range(1, cols):
            col = j
            row = 0
            holdM = matrix[row][col]
            while row < rows-1 and col < cols-1:
                col += 1
                row += 1
                if holdM != matrix[row][col]:
                    return False
                holdM = matrix[row][col]
        return True