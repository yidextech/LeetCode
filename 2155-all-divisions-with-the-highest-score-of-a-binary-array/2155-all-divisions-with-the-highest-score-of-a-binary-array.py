class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        res = defaultdict(int)
        max_score = float('-inf')

        n = len(nums)

        count0 = nums.count(0)
        count1 = n - count0
        for i in range(n+1):
            if i == 0:
                nums_left = 0
                nums_right = count1
            elif i == n:
                nums_left = count0
                nums_right = 0
            else:
                if  nums[i-1] == 0:
                    nums_left += 1
                else:
                    nums_right -= 1
            
            score = nums_left + nums_right
            if score > max_score:
                max_score = score
                res.clear()
                res[max_score]= [i]
            elif score == max_score:
                res[max_score].append(i)
        
        return res[max_score]
            