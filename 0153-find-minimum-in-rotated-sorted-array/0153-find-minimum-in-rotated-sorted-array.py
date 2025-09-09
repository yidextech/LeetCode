class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        min_num = float("inf")
        while l <= r:
            mid = (l+r)//2 # l + (r-l)/2
            min_num = min(min_num, nums[mid])
            if nums[mid] < nums[l] and nums[mid] < nums[r]:
                if nums[l] > nums[r]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[l] < nums[r]:
                    min_num = min(min_num,nums[l])
                    r = mid-1
                else:
                    min_num =  min(min_num, nums[r])
                    l = mid+1
            
        return min_num
