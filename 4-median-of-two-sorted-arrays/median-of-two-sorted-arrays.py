class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        final = sorted(nums1 + nums2)
        n = len(final)
        if len(final) % 2 == 1:
            return float(final[n//2])
        return (final[(n//2)-1] + final[(n//2)]) /2.0