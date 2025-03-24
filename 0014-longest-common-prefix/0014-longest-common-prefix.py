class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()
        
        check  = strs[0]
        

        for i in range(1, len(strs)):
            prefix = ""
            j = 0
            while j < len(check) and j < len(strs[i]):
                if check[j] == strs[i][j]:
                    prefix += check[j]
                else: 
                    check = prefix
                    if check  == "":
                        return check
                    break
                j +=1
            check = prefix
        return check
