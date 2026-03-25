"""
4. Median of Two Sorted Arrays
Hard
Topics
premium lock icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKth(n1, n2, k):
            if len(n1) > len(n2):
                return getKth(n2, n1, k)
            if not n1:
                return n2[k-1]
            if k == 1:
                return min(n1[0], n2[0])
            p1 = min(k // 2, len(n1))
            p2 = k - p1
            
            if n1[p1 - 1] < n2[p2 - 1]:
                return getKth(n1[p1:], n2, k - p1)
            else:
                return getKth(n1, n2[p2:], k - p2)
        
        n = len(nums1) + len(nums2)
        left = (n + 1) // 2
        right = (n + 2) // 2
        return (getKth(nums1, nums2, left) + getKth(nums1, nums2, right)) / 2.0
    
solution = Solution()
print(solution.findMedianSortedArrays([1,3], [2])) # 2.00000

"""
This question is ridiculous, I will resolve this question util I really master it.
"""
