# Problem: 2302. Count Subarrays With Score Less Than K [https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/?envType=daily-question&envId=2025-04-28]
# Difficulty: Hard

# My solution: O(n), O(1)
# 1. Initialize variables to track the left pointer, current sum, and count of valid subarrays.
# 2. Iterate through the array with a right pointer.
# 3. For each element, add it to the current sum.
# 4. While the current sum multiplied by the length of the subarray is greater than or equal to k, move the left pointer to the right and subtract the leftmost element from the current sum.
# 5. Count the number of valid subarrays ending at the current position by adding (right - left + 1) to the count.
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        current_sum = 0
        count = 0

        for right, num in enumerate(nums):
            current_sum += num

            while left <= right and current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
                
            count += (right - left + 1)

        return count
    
# Intuition: Check all required subarrays and count the number of valid ones.