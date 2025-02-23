class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        result =  []
        for n in nums:
            result.append(n**2)

        output = []
        left = 0
        right = len(result)-1

        while(right >= left):
            if result[right] >= result[left]:
                output.append(result[right])
                right -= 1
            else:
                output.append(result[left])
                left +=1
        return output[::-1]