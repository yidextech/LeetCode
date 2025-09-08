class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        check = {}

        for i in range(len(nums)):
            if nums[i] in check:
                j = check[nums[i]]
                if abs(i-j) <=k:
                    return True
            check[nums[i]] = i
        return False
        