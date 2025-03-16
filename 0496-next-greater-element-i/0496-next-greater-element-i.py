class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        

        for num1 in nums1:

            for num2 in nums2[nums2.index(num1):]:
                x = None
                if num2 > num1:
                    x = num2
                    break
            if x:
                output.append(x)
            else:
                output.append(-1)

        return output