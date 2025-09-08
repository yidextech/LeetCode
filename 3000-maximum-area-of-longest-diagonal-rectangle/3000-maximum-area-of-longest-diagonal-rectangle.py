class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxd = 0
        maxarea = 0
        for dim in dimensions:
            l,w = dim[0], dim[1]
            d1 = l**2 + w**2
            if d1 > maxd:
                maxd = d1
                maxarea = l*w
            elif d1 == maxd:
                if l*w > maxarea:
                    maxarea = l*w
        return maxarea