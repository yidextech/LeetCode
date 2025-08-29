class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        check = set()
        longest = 0
        n = len(s)
        for i in range(n):
            count = 0
            j = i
            while j<n and s[j] not in check:
                check.add(s[j])
                count += 1
                j += 1
            longest = max(longest, count)
            check.clear()
        return longest