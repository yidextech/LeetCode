class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(cur_str,open_count,close_count,n,result):
            #condition for a valid
            #0<=closecount<=opencount<=n
            if len(cur_str) == 2*n:
                result.append(cur_str)
                return
            if open_count < n:
                backtrack(cur_str+'(', open_count+1, close_count,n,result)
            if close_count < open_count:
                backtrack(cur_str+')', open_count, close_count+1,n, result)
        
        result = []
        backtrack("",0,0,n,result)
        return result