class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        dup = defaultdict(int)
        res = 0
        for i, num in enumerate(nums):
            if num in dup:
                dup[num].append(i)
            else:
                dup[num] = [i]

        for indxs in dup.values():
            for i in range(len(indxs)):
                for j in range(i+1, len(indxs)):
                    if (indxs[i]*indxs[j]) % k == 0:
                        res += 1
        return res