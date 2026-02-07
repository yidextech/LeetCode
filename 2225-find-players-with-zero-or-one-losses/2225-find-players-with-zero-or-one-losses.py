class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        losers = defaultdict(int)
        winners = set()
        for player in matches:
            #checking for the winner
            if player[0] not in losers:
                winners.add(player[0])
                
            #checking for the loser 
            losers[player[1]] += 1
            if player[1] in winners:
                winners.discard(player[1])
        print(winners)
        winners = list(winners)
        winners.sort()
        loser_list = []
        for loser, i in losers.items():
            if i == 1:
                loser_list.append(loser)
        
        loser_list.sort()
        return [winners, loser_list]
        

        

