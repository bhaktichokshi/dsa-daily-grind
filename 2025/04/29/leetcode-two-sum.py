# 1. Two Sum [https://leetcode.com/problems/two-sum/]
# Difficulty: Easy

from typing import List

# My solution: O(n), O(n)
# 1. Create a dictionary to store the indices of the numbers.
# 2. Iterate through the list of numbers:
#  - For each number, calculate its complement (target - number).
#  - Check if the complement is already in the dictionary.
#  - If it is, return the indices of the current number and its complement.
# 3. If not, store the current number and its index in the dictionary.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # num -> index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i