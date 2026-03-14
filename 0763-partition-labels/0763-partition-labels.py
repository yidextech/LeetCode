class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        i = 0
        j = 0

        res = []
        while i < len(s):
            k = s.rfind(s[i])
            while j < k:
                indx = s.rfind(s[j])
                k = max(k, indx)
                j += 1
            res.append(j-i+1)
            i = k+1
            j = k+1
        
        return res