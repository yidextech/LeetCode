class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        nums_count = defaultdict(int)

        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
        
        for i, j in nums_count.items():
            if j > (len(nums)//3):
                res.append(i)
        return res