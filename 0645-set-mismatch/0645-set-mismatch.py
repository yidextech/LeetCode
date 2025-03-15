class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dups = set()
        output = []
        for num in nums:
            if num in dups:
                output.append(num)
            else:
                dups.add(num)

        output.extend(list(set(range(1, len(nums)+1)).difference(set(nums))))
        return output
