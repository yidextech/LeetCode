class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict= Counter(nums)

        for num, c in nums_dict.items():
            if c > (len(nums)//2):
                return num