class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        maxArea =  0
        while l<r:
            w = r-l #width
            h = min(height[l], height[r]) #height
            area = w*h 
            maxArea =max(maxArea, area)
            if height[l] < height[r]:
                l +=1
            else:
                r -= 1
        return maxArea
