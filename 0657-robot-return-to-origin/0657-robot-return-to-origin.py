class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = Counter(moves)
        if count['U'] == count['D'] and count['R'] == count['L']:
            return True
        return False