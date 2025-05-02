# Problem: 838. Push Dominoes [https://leetcode.com/problems/push-dominoes/description/?envType=daily-question&envId=2025-05-02]
# Difficulty: Medium

from typing import List

# My solution: O(n), O(n)
# 1. Create a list to store the forces acting on each domino.
# 2. Iterate through the dominoes from left to right:
#    - If a domino is 'R', set the force to a large number.
#    - If a domino is 'L', reset the force to 0.
#    - If a domino is '.', decrease the force by 1.
# 3. Iterate through the dominoes from right to left:
#    - If a domino is 'L', set the force to a large number.
#    - If a domino is 'R', reset the force to 0.
#    - If a domino is '.', decrease the force by 1.
# 4. Construct the result based on the forces:
#    - If the force is positive, the domino will fall to the right ('R').
#    - If the force is negative, the domino will fall to the left ('L').
#    - If the force is zero, the domino will remain upright ('.').
# 5. Return the final string representing the state of the dominoes.
# # Intuition: The forces acting on each domino determine its final state.
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        
        # Left to right (force from 'R')
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # Use a large number as max force
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
        
        # Right to left (force from 'L')
        force = 0
        for i in reversed(range(n)):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
        
        # Construct result
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')
        
        return ''.join(result)