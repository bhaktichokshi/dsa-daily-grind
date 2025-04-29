# Problem: 2962. Count Subarrays Where Max Element Appears at Least K Times [https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29]
# Difficulty: Medium

# My solution: O(n), O(1)
# 1. Find the maximum value in the array.
# 2. Initialize pointers and counters.
# 3. Iterate through the array with a right pointer.
# 4. If the current number is equal to the maximum value, increment the count of max occurrences.
# 5. While the count of max occurrences is greater than or equal to k, move the left pointer to the right and decrement the count if necessary.
# 6. Count the number of valid subarrays ending at the current position by adding (left) to the count.
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        left = 0
        count = 0
        max_count = 0

        for right in range(len(nums)):
            if nums[right] == max_val:
                max_count += 1

            while max_count >= k:
                if nums[left] == max_val:
                    max_count -= 1
                left += 1

            count += left
        return count
    

    # this was really hard idk why