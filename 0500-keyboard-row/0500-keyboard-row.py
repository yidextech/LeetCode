class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row1 = "qwertyuiop"
        row2 = "asdfghjfkl"
        row3 = "zxcvbnm"


        output = []
        for i in range(len(words)):
            
            if set(words[i].lower()).issubset(set(row1)):
                output.append(words[i])
            elif set(words[i].lower()).issubset(set(row2)):
                output.append(words[i])
            elif set(words[i].lower()).issubset(set(row3)):
                output.append(words[i])
        return output
