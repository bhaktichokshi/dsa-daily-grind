# [2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29)

### TL:DR
When max_count >= k, all subarrays from the current left to end of array with this right are valid, because adding more elements won’t reduce the max_count.

Track how many times the max value appears in a window.
Each time it appears ≥ k, all subarrays from left to right are valid.

### also, this was hard so watch the neetcode solution: http://youtube.com/watch?v=CZ-z1ViskzE

# [2799. Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/)

Step 1: What’s a complete subarray?

If the whole array has 3 distinct elements — say {1, 2, 3} — then any subarray that contains all three is a complete subarray.

So first thing we do? Count how many distinct values the full array has. In Python, that’s just len(set(nums)).

Step 2: Sliding window time.

Now we slide through the array using two pointers — left and right — and we maintain a hashmap to count the frequency of each number in the current window.

As we move the right pointer forward, we add numbers to our frequency map. If the size of that map (i.e., how many keys) equals the total number of unique elements — boom, we found a complete window.

Here’s the beautiful trick: Once the window is complete, every extension of that window to the right is also complete.

So we add len(nums) - right to our count — that’s how many complete subarrays start at left and end at or after right.

Then we try to move left forward to find more valid windows.

Rinse and repeat.