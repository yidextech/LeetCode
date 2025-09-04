class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights = [0] + heights + [0]
        stack = [0]

        max_area = 0
        for i in range(1,len(heights)):
            while stack and  heights[i] < heights[stack[-1]]:
                indx = stack.pop()
                area = heights[indx] * (i-stack[-1]-1)
                max_area = max(area, max_area)
            stack.append(i)
        return max_area