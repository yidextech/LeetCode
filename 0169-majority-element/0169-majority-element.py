class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        c = len(nums)//2
        for item,i in Counter(nums).items():
            if i > c:
                return item