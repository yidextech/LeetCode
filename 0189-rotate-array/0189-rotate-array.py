class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - (k%n)

        new_nums = nums[i:]
        del nums[i:]

        for k in range(len(new_nums)-1, -1, -1):
            nums.insert(0, new_nums[k])