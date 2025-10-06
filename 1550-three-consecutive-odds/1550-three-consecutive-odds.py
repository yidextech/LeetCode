class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for ar in arr:
            count
            if ar%2 != 0:
                count += 1
                if count == 3:
                    count = 0
                    return True
            else:
                count = 0
        return False
            