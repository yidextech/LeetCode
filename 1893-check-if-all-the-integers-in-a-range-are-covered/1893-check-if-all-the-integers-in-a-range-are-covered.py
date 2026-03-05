class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        lr = set(range(left, right+1))
        i = 0
        while lr and i < len(ranges):
            r = ranges[i]
            c = set(range(r[0], r[1]+1))
            lr -= c
            i += 1

        if not lr:
            return True
        return False
        
