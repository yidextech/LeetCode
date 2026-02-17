class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        row = len(mat)
        col = len(mat[0])
        n = row+col-2

        res = []
        for i in range(n+1):
            #odd
            if i%2 != 0:
                for j in range(min(i+1,row)):
                    indx = i-j
                    if indx < col:
                        res.append(mat[j][indx])
            #even
            else:
                for j in range(min(i,row-1), -1, -1):
                    indx = i-j
                    if indx < col:
                        res.append(mat[j][indx])

        return res

