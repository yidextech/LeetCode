class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        def winner(arr,idx):
            nonlocal k
            if len(arr) == 1:
                return arr[0]
            rmf = (idx+k-1)%len(arr)
            arr.pop(rmf)
            return winner(arr, rmf)
        
        return winner(friends,idx=0)