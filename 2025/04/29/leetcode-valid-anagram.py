# Problem: 242. Valid Anagram [https://leetcode.com/problems/valid-anagram/]
# Difficulty: Easy

# My solution: O(n), O(1)
# 1. Check if the lengths of the two strings are equal. If not, return False.
# 2. Create a count array of size 26 (for lowercase letters).
# 3. Iterate through both strings simultaneously:
#  - For each character in the first string, increment the corresponding index in the count array.
#  - For each character in the second string, decrement the corresponding index in the count array.
# 4. Finally, check if all values in the count array are zero. If they are, return True; otherwise, return False.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26  # For 'a' to 'z'

        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1

        return all(c == 0 for c in count)