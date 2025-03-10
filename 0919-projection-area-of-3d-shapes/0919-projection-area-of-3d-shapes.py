class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        top = sum(1 for row in grid for val in row if val > 0)
      
        front = sum(max(row) for row in grid)

        side = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        
        return top + front + side