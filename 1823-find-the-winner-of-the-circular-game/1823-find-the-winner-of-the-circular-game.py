class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        count = 0
        i= 0
        players = list(range(1, n+1))
        while len(players) > 1:
            count += 1
            if count == k:
                count =0 
                del players[i]
            else:
                i += 1
                i %= len(players)

        return players[0]