import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        intersection = []
        for k, v in (c1 & c2).items():
            intersection.extend([k] * v)
        return intersection
