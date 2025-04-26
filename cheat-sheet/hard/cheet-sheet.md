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