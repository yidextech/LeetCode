class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        arr = list(range(1, n+1))
        def winner(arr, indx):
            if len(arr) == 1:
                return arr[0]
            rmf = (indx+k-1)%len(arr)
            arr.pop(rmf)
            return winner(arr, rmf)
        
        return winner(arr, indx=0 )
