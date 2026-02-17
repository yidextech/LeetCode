class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        visited =  set()

        for i in range(row):
            for j in range(col):
                next_location = (i,j)
                while next_location not in visited:
                    visited.add(next_location)
                    new_location =  (next_location[1], col-next_location[0]-1)
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[new_location[0]][new_location[1]]
                    matrix[new_location[0]][new_location[1]] = temp
                    next_location = new_location
