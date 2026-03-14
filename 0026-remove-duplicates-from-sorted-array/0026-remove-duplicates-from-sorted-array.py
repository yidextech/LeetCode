class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        c = Counter(nums)

        def solution(i, nums):
            if i >= len(nums):
                return 
            
            j = c[nums[i]]
            if j >1:
                del nums[i+1:i+j]
            solution(i+1, nums)
        solution(0, nums)