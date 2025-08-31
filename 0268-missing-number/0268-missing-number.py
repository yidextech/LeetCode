class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        check = set(x for x in range(n+1))
        nums = set(nums)

        missing = list(check-nums)
        return missing[0]