class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range (len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        if len(nums1)%2 == 0:
            x = len(nums1)//2
            return (nums1[x-1]+nums1[x])/2

        else:
            y = (len(nums1)+1)//2
            return nums1[y-1]