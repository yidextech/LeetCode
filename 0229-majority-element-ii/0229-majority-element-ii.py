class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        nums_count = Counter(nums)
        
        for num, c in nums_count.items():
            if c > (len(nums)//3):
                res.append(num)
        return res