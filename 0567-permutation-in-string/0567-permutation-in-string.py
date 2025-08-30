class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n,m = len(s1), len(s2)

        if n > m:
            return False

        s1_window = Counter(s1)
        s2_window = Counter(s2[:n])

        if s2_window == s1_window:
            return True

        for i in range(n,m):
            s2_window[s2[i]] += 1
            s2_window[s2[i-n]] -= 1

            if s1_window == s2_window:
                return True
        return False


