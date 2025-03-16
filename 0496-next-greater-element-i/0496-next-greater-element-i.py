class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        

        for num1 in nums1:
            x = nums2.index(num1)
            y = [a for a in nums2[x:] if a>num1]
            if y:
                output.append(y[0])
            else:
                output.append(-1)
        return output