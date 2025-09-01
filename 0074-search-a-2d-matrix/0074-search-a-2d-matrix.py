class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row,col =(len(matrix), len(matrix[0]))
        l = [0,0]
        r = [row-1, col-1]

        while (l[0] + l[1]) <= (r[0]+r[1]):
            mid = [ (l[0]+r[0])//2, (l[1]+r[1])//2]
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] < target:
                if mid[1] == col-1:
                    l = [mid[0]+1, 0]
                else:
                    l[1] += 1
            else:
                if mid[1] == 0:
                    r = [mid[0]-1, col-1]
                else:
                    r[1] -= 1
        return False
