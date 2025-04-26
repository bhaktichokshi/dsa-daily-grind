# Problem: 2444. Count Subarrays With Fixed Bounds [https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/?envType=daily-question&envId=2025-04-26]
# Difficulty: Hard

# My solution:
# 1. Initialize variables to track the last seen positions of minK, maxK, and invalid numbers.
# 2. Iterate through the array, updating the positions based on the current number.
# 3. If the current number is outside the bounds, update the invalid position.
# 4. If the current number is minK or maxK, update the respective position.
# 5. Calculate the number of valid subarrays ending at the current position.
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        min_pos = max_pos = invalid_pos = -1

        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                invalid_pos = i
            
            if num == minK:
                min_pos = i
            
            if num == maxK:
                max_pos = i
            
            # Only if both minK and maxK have been seen
            answer += max(0, min(min_pos, max_pos) - invalid_pos)

        return answer