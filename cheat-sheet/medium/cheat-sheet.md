# [2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29)

### TL:DR
When max_count >= k, all subarrays from the current left to end of array with this right are valid, because adding more elements won’t reduce the max_count.

Track how many times the max value appears in a window.
Each time it appears ≥ k, all subarrays from left to right are valid.

### also, this was hard so watch the neetcode solution: http://youtube.com/watch?v=CZ-z1ViskzE