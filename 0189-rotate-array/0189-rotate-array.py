class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def solution(k, arr):
            if k == 0:
                return 
            k -= 1
            front = arr.pop()
            arr.insert(0, front)
            solution(k, arr)
        
        solution(k, nums)