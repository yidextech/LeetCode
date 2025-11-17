class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        distance = []

        for i in range(len(nums)):
            if nums[i] == 1:
                distance.append(i)

        for i in range(1, len(distance)):
            check = distance[i] - distance[i-1] - 1
            if check < k:
                return False
        return True