class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxword = 0

        for sentence in sentences:
            word_count = sentence.count(" ")+1
            maxword = max(word_count, maxword)
        return maxword