# Problem: 1920. Build Array from Permutation [https://leetcode.com/problems/build-array-from-permutation/?envType=daily-question&envId=2025-05-06]
# Difficulty: Easy

from typing import List

# My solution: O(n), O(n)
# 1. Create an array of the same length as nums to store the result.
# 2. Iterate through the nums array, and for each index i, set the value at index i in the result array to nums[nums[i]].
# 3. Return the result array.
# Intuition: The result array is built by applying the permutation defined by nums twice.
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans