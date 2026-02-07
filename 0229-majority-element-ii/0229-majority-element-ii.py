class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = len(nums)//3
        res = []
        for num,i in Counter(nums).items():
            if i > c:
                res.append(num)
        return res