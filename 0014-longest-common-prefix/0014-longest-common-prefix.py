class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for short in strs:
            if len(common)>len(short):
                common = short

        print(common)
        for word in strs:
            prefix = ""
            i = 0
            while i < len(common) and common[:i+1] in word[:i+1]:
                prefix = common[:i+1]
                i += 1
            if not prefix:
                return ""
            common = prefix
        
        return common
