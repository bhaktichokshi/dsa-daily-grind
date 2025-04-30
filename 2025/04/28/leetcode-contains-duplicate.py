# Problem: 217. Contains Duplicate [https://leetcode.com/problems/contains-duplicate/]
# Difficulty: Easy

from typing import List

# My solution: O(n), O(n)
# 1. Convert the list to a set, which removes duplicates.
# 2. Compare the length of the set with the original list.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
    
# Alt Solutions
# 1. Use sort and check adjacent elements. O(nlogn) but O(1) for space
# 2. Use a dictionary/set/hash to count occurrences. O(n) for both time and space. 