"""
846. Hand of Straights
Medium
Topics
premium lock icon
Companies
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
"""

from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for h in sorted(count):
            if count[h] > 0:
                start_count = count[h]
                for i in range(h, h + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        return True
    
solution = Solution()
print(solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3)) # True
print(solution.isNStraightHand([1,2,3,4,5], 4)) # False

"""
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
