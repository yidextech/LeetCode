class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        rows = len(img)
        cols = len(img[0])

        new_img = [[0]*cols for _rows in img]
        for i in range(rows):
            for j in range(cols):
                cell_total = img[i][j]
                count = 1
                if i > 0:
                    cell_total += img[i-1][j]
                    count += 1
                    if j > 0:
                        cell_total += img[i-1][j-1]
                        count += 1
                    if j < cols-1:
                        cell_total += img[i-1][j+1]
                        count += 1
                if i < rows-1:
                    cell_total += img[i+1][j]
                    count += 1
                    if j > 0:
                        cell_total += img[i+1][j-1]
                        count += 1
                    if j < cols-1:
                        cell_total += img[i+1][j+1]
                        count += 1
                if j > 0:
                        cell_total += img[i][j-1]
                        count += 1
                if j < cols-1:
                        cell_total += img[i][j+1]
                        count += 1
                new_img[i][j] = (cell_total//count)

        return new_img