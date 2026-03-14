class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        i= 0
        j = len(skill)-1
        res = 0

        prev = 0

        
        while j > i:
            cur = skill[i] + skill[j]
            if prev and prev != cur:
                return -1
            res += (skill[i]*skill[j])
            prev = cur
            j -= 1
            i += 1

        return res
