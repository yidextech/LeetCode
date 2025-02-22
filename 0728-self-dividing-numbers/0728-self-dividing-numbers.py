class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        output = []

        for i in range(left, right+1):
            if len(str(i)) > 1 and "0" not in str(i):
                for x in str(i):
                    insert = True
                    if i % int(x) != 0:
                        insert = False
                        break
                if insert:
                    output.append(i)
            if len(str(i)) == 1:
                output.append(i)
        return output
