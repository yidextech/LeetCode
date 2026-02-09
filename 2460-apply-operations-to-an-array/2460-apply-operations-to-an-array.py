class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        i = 0
        j = len(nums)-1

        while i < j:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                j -= 1
            elif nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                i += 1
            else:
                i+= 1
        return nums