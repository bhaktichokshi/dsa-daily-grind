# Problem: 3392. Count Subarrays of Length Three With a Condition [https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/?envType=daily-question&envId=2025-04-27]
# Difficulty: Easy

from typing import List

# My solution: O(n), O(1)
# 1. Start at index 0.
# 2. While you’re not at the last two elements:
#  - Grab 3 numbers starting at your current position.
#  - Check if the second number is odd. If yes, skip to the next index.
#  - Check the magic condition: (first + third) == (half of second).
#  - If yes, add to your “count of good subarrays” tally.
# 3. Return the final tally.
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):  # Only go till third-last element
            if nums[i+1] % 2 == 1:
                continue
            if nums[i] + nums[i+2] == nums[i+1] / 2:
                count += 1
        return count