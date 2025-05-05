class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        groups = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = i+j
                groups[key].append(mat[i][j])
    
        print(groups)
        turn = 0
        output =[]
        for key, value in groups.items():
            if not turn:
                output.extend(value[::-1])
            else:
    
                output.extend(value)
            turn = 1-turn
        return output