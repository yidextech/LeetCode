class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eatBanana(k):
            hours = 0
            for pile in piles:
                hours += pile //k
                if pile % k != 0:
                    hours+= 1
                if hours>h:
                    return False
            return True

        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            mid = (left+right)//2
            if eatBanana(mid):
                ans = mid
                right = mid -1
            else:
                left = mid +1
        return ans

