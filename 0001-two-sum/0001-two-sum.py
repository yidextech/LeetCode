class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        old_nums = nums[:]
        nums.sort()

        l = 0
        r = len(nums)-1

        while l<r:
            if nums[l] + nums[r] == target:
                i = old_nums.index(nums[l])
                j = old_nums.index(nums[r])
                if i <=j:
                    old_nums.pop(i)
                    j = old_nums.index(nums[r])+1
                return [i,j]
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1