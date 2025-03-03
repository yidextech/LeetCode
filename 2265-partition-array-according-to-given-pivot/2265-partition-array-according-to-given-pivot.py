class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        lstack = []
        rstack = []
        isPivot = []
        for i in nums:
            if i < pivot:
                lstack.append(i)
            elif i > pivot:
                rstack.append(i)
            elif i == pivot:
                isPivot.append(i)
        lstack.extend(isPivot)
        lstack.extend(rstack)
        return lstack