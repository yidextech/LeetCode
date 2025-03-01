class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        stack = []
        for i in nums:
            if nums.count(i) > 1:
                if i not in stack:
                    stack.append(i)
                    if len(stack) == 2:
                        break
        return stack
            