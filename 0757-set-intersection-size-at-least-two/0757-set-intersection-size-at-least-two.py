class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        chosen = []
        
        for start, end in intervals:
            # count how many chosen points lie in this interval
            count = 0
            for p in reversed(chosen):
                if p < start:
                    break
                count += 1
                if count == 2:
                    break
            
            # if we need to add points
            needed = 2 - count
            while needed > 0:
                # add from the largest possible (end → downward)
                point = end - (needed - 1)
                chosen.append(point)
                needed -= 1
        
        return len(chosen)