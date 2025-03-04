class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        inter = list(set(nums1).intersection(set(nums2))) 
        newInter = []
        for i in inter:
            x = min(nums1.count(i), nums2.count(i))
            for j in range(x):
                newInter.append(i)
        return newInter

