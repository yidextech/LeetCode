class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = Counter(t)
        s_count = defaultdict(int)
        have,need = 0, len(t_count)
        l = 0
        ans = ""
        len_ans = len(s)

        for r in range(len(s)):
            c = s[r]
            s_count[c] += 1
            if s_count[c] == t_count[c]:
                have += 1
            while (have == need):
                if len_ans >= (r-l+1):
                    ans = s[l:r+1]
                    len_ans = r-l+1
                s_count[s[l]] -= 1
                if s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l +=1
                while l < len(s) and s[l] not in t_count:
                    l += 1
        return ans
