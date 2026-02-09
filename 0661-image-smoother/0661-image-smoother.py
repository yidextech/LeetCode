class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        new_img = [[0 for col in range(len(img[0]))] for row in range(len(img))]
        
        for rows in range(len(img)):
            for cols in range(len(img[0])):
                total = 0
                num = 0
                for i in range(rows-1, rows+2):
                    if i < 0 or i >= len(img):
                        continue
                    for j in range(cols-1, cols+2):
                        if j < 0 or j >= len(img[0]):
                            continue 
                        num += 1
                        total += img[i][j]

                new_img[rows][cols] = total//num
                
        return new_img