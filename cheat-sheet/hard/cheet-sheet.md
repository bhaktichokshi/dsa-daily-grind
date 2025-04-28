# [2444. Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/?envType=daily-question&envId=2025-04-26)

### TL;DR 
Track min, track max, track bads. Subarrays = min(last min, last max) - last bad. Easy win.

### 1. Set up your trackers
```bash
last_min = -1 
last_max = -1
last_invalid = -1
count = 0
``` 
last_min: Last index where minK appeared
last_max: Last index where maxK appeared
last_invalid: Last index where a bad number appeared (outside [minK, maxK])

### 2. Walk through the array
```bash
for i, num in enumerate(nums):
    if num < minK or num > maxK:
        last_invalid = i
    if num == minK:
        last_min = i
    if num == maxK:
        last_max = i
    count += max(0, min(last_min, last_max) - last_invalid)
```

### 3. At each step, THINK:
- Did I see minK yet?
- Did I see maxK yet?
- Did I hit a bad number recently?
- If both minK and maxK exist after last_invalid ➔ you can form new valid subarrays ending here! 🎯

### Mental Model:

Imagine you are…
- “holding hands” with the last minK and maxK you saw
- “cutting off” anyone before the last invalid number
- counting how many valid “endings” you can have at every step!

```bash
max(0, min(last_min, last_max) - last_invalid)
```

# [2302. Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/?envType=daily-question&envId=2025-04-28)

### TL:DR
Slide a window across nums, grow it, and shrink it if (sum * length) >= k.
At every step, add (right - left + 1) to your count.
O(n) time, O(1) space. Expand ➡️ Shrink ➡️ Count. Easy dubs.

### Steps
1. Initialize left = 0, current_sum = 0, count = 0.
2.	For each right in range of nums:
    - Add nums[right] to current_sum.
	- While current_sum * window_length >= k, shrink window from left:
	- Subtract nums[left] from current_sum.
	- Move left by 1.
	- After shrinking (if needed), add (right - left + 1) to count.
3.	Return count.