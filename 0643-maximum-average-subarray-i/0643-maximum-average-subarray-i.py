class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        cur_sum = sum(nums[0:k])
        maxAvg = cur_sum / k
        for i in range(1, (len(nums)-k+1)):
            new_sum = cur_sum - nums[i-1] + nums[i+k-1]
            maxAvg = max(maxAvg, new_sum/k)
            cur_sum = new_sum
        return maxAvg