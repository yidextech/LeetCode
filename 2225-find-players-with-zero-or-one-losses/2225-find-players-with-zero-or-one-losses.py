class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = set()
        losers = set()
        one_losers  = set()

        for match in matches: 
            if match[0] not in losers:
                winners.add(match[0])
            #loser
            if match[1] in losers:
                one_losers.discard(match[1])
            else:
                losers.add(match[1])
                one_losers.add(match[1])

        winners = list(winners-losers)
        winners.sort()
        one_losers = list(one_losers)
        one_losers.sort()
        
        return [winners, one_losers]