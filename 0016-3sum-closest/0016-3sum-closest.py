class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        
        
        greater =  999999
        smaller = -999999


        nums.sort()

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            
            while(l < r):
                if nums[i] + nums[l] + nums[r] > target:
                    if nums[i] + nums[l] + nums[r] < greater:
                        greater = nums[i] + nums[l] + nums[r]
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < target:
                    if nums[i] + nums[l] + nums[r] > smaller:
                        smaller = nums[i] + nums[l] + nums[r]
                    l += 1
                else:
                    return target
        if abs(smaller-target) < abs(greater-target):
            return smaller
        else:
            return greater