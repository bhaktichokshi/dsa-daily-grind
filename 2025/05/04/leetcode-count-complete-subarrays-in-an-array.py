# Problem: 2799. Count Complete Subarrays in an Array [https://leetcode.com/problems/count-complete-subarrays-in-an-array/]
# Difficulty: Medium

from typing import List

# My solution: O(n), O(n)
# 1. Count the number of unique elements in the array.
# 2. Use a sliding window approach to find all subarrays that contain all unique elements.
# 3. For each valid subarray, count the number of complete subarrays.
# 4. Return the total count of complete subarrays.
# 5. The sliding window approach ensures that we only iterate through the array once, making it efficient.
# 6. The dictionary is used to keep track of the frequency of each element in the current window.
# 7. The left pointer is moved to shrink the window when all unique elements are present.
# 8. The count of complete subarrays is updated by adding the number of remaining elements in the array.
# 9. The final count is returned as the result.
# Intuition: The number of complete subarrays is determined by the number of unique elements in the array and the frequency of each element in the current window.
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))  # Still okay, no external lib
        count = 0
        left = 0
        freq = {}  # Regular dict

        for right in range(len(nums)):
            num = nums[right]
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            while len(freq) == total_unique:
                count += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return count