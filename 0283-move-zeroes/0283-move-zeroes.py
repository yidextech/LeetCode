class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        opns = 0

        i = 0
        while opns <= len(nums) and i < len(nums):
            opns += 1
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
