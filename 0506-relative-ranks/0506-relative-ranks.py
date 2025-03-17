class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        output = [0]*len(score)

        sortedScore = score.copy()
        sortedScore.sort(reverse=True)

        j = 1
        for ss in sortedScore:
            i = score.index(ss)

            if j == 1:
                output[i] = "Gold Medal"
            elif j == 2:
                output[i] = "Silver Medal"
            elif j == 3:
                output[i] = "Bronze Medal"
            else:
                output[i] = str(j)
            
            j += 1
        return output