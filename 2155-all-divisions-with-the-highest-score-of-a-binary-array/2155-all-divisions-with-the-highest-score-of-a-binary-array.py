class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        res = defaultdict(int)
        max_score = float('-inf')

        n = len(nums)
        for i in range(n+1):
            if i == 0:
                nums_left = 0
                nums_right = nums.count(1)
            elif i == n:
                nums_left = nums.count(0)
                nums_right = 0
            else:
                nums_left = nums[:i].count(0)
                nums_right = nums[i:].count(1)
            
            score = nums_left + nums_right
            if score > max_score:
                max_score = score
                res.clear()
                res[max_score]= [i]
            elif score == max_score:
                res[max_score].append(i)
        
        return res[max_score]
            