# Problem: 1007. Minimum Domino Rotations For Equal Row [https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/?envType=daily-question&envId=2025-05-03]
# Difficulty: Medium

from typing import List

# My solution: O(n), O(1)
# 1. Count the occurrences of each number in the first row.
# 2. For each number, check if it can be the target number for both rows.
# 3. If it can, calculate the number of rotations needed to make both rows equal.
# 4. Return the minimum number of rotations needed.
# 5. If no number can be the target, return -1.
# Intuition: The minimum number of rotations needed to make both rows equal is determined by the number of occurrences of each number in both rows.
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')  # not possible
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        res = min(check(tops[0]), check(bottoms[0]))
        return res if res != float('inf') else -1