# [3392. Count Subarrays of Length Three With a Condition](https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/submissions/1619641396/?envType=daily-question&envId=2025-04-27)

### TL;DR
If the middle guy’s odd, skip it. If the first and third are smart enough to team up and half the middle, count it!

### Steps
1. Initialize a count variable to track valid subarrays.
2. Loop from 0 to len(nums) - 3 (because we need 3 elements at least).
3. For each window:
    - Check if the middle number is even (optimization!).
- Check if first + third == middle // 2 
4. Return the final count.

# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

| Approach                     | Time Complexity | Space Complexity | Good for Interviews?          |
|:------------------------------|:----------------|:-----------------|:-------------------------------|
| Traverse every pair           | O(n²)            | O(1)              | 🚫 No (only as "brute force")   |
| Traverse with early break     | O(n²)            | O(1)              | 🚫 Meh (still bad scaling)      |
| Sort and check neighbors      | O(n log n)       | O(1) (if in-place)| ✅ Yes (mention tradeoffs)      |
| Set (hashing)                 | O(n)             | O(n)              | ✅✅✅ YES (absolute best)       |

-------------------------------------------------------
| Method                        | Code Size      | Speed     | Vibe Check                          |
|:-------------------------------|:---------------|:----------|:------------------------------------|
| Set with loop (`seen.add()`)    | More verbose   | O(n)      | Traditional, very readable          |
| Set with length compare (`len(nums) > len(set(nums))`) | ✨ One-liner | O(n) | Clean, cheeky, and interview GOLD 🌟 |


# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

### TL;DR
Create a hashmap like storage. Add count if character occurs in first word, subtract if it occurs in second. That way, ideally it should be zero-zero so check for that.

# [1. Two Sum](https://leetcode.com/problems/two-sum)

### TL;DR
Use a hashmap to track seen values. For each num, check if target - num exists.

# [1295. Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=daily-question&envId=2025-04-30)

### TL;DR
Convert each number to a string, check if its length is even, and count how many pass. One-liner with a generator — clean and efficient.

# [1007. Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/?envType=daily-question&envId=2025-05-03)

# TL;DR
Count how many pairs of equivalent dominoes exist (e.g., [1,2] ≡ [2,1]).

⚠️ Why not sum(1 for ...) or sum(v for ...)?
- sum(1 for ...) → counts how many types had duplicates ✅
- sum(v for ...) → counts how many total repeated dominoes ❌
- But the problem wants how many total pairs of equivalent dominoes 🔥