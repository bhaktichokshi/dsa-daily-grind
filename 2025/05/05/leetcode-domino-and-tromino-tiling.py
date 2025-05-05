# Problem: 790. Domino and Tromino Tiling [https://leetcode.com/problems/domino-and-tromino-tiling/description/?envType=daily-question&envId=2025-05-05]
# Difficulty: Medium

from typing import List

# My solution: O(n), O(n)
# 1. Use dynamic programming to keep track of the number of ways to tile the board.
# 2. Define a dp array where dp[i] represents the number of ways to tile a board of length i.
# 3. Initialize the base cases: dp[0] = 1 (empty board), dp[1] = 1 (one way to place a domino), dp[2] = 2 (two ways to place two dominoes).
# 4. For lengths greater than 2, calculate the number of ways to tile the board using the recurrence relation:
#    dp[i] = 2 * dp[i - 1] + dp[i - 3]
# 5. The recurrence relation accounts for the two ways to place a domino and the additional ways to place a tromino.
# 6. Return dp[n] as the final answer, which is the number of ways to tile a board of length n.
# 7. Use modulo 10^9 + 7 to handle large numbers.
# Intuition: The number of ways to tile a board of length n can be derived from the number of ways to tile shorter boards.
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp = [0] * (n + 1)
        dp[0] = 1  # Empty board
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n + 1):
            dp[i] = (
                2 * dp[i - 1] + 
                dp[i - 3]
            ) % MOD

        return dp[n]
    

# Initial Wron Solution
class Solution:
    def numTilings(self, n: int) -> int:
        count = 0
        if (2*n) - ((2*n// 2)*2) == 0:
            count += (2*n// 2) 

        if (2*n) - (((2*n// 3))*3) == 0:
            count += (2*n// 3)
        return count
        