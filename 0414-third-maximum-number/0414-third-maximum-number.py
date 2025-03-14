class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        dups = set()
        count = 0
        nums.sort(reverse=True)
        nondups = []
        for num in nums:
            if num in dups:
                pass
            else:
                dups.add(num)
                nondups.append(num)
                count += 1
                if count == 3:
                    return num
        return nondups[0]
            