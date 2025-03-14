class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupHash ={}

        for i in range(len(nums)):
            if nums[i] in dupHash:
                if abs(dupHash[nums[i]] - i) <= k:
                    return True
                else:
                    dupHash[nums[i]] = i
            else:
                dupHash[nums[i]] = i
        return False