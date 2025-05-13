"""
Problem #3335: Total Characters in String After Transformation

Given a string s consisting of lowercase English letters and an integer t, return the total number of characters that will exist in s after t transformations modulo 10^9 + 7.

In one transformation, each character is transformed as follows:
- For letters 'a' to 'y', the character is changed to the next letter. For example, 'a' becomes 'b', 'b' becomes 'c', and so on.
- The letter 'z' is transformed into both 'a' and 'b', essentially creating two characters.

Example 1:
Input: s = "abc", t = 2
Output: 6
Explanation: 
After 1 transformation, "abc" becomes "bcd".
After 2 transformations, "bcd" becomes "cde".
Total characters = 3.

Example 2:
Input: s = "z", t = 2
Output: 4
Explanation: 
After 1 transformation, "z" becomes "ab".
After 2 transformations, "ab" becomes "bc".
Total characters = 2 + 2 = 4.

Approach:
- For each transformation, we track how many characters each letter produces.
- Initially, each character in the original string contributes 1 character.
- For letters 'a' to 'y', they transform into the next letter.
- For letter 'z', it transforms into both 'a' and 'b'.
- After computing the number of characters each letter produces after t transformations,
  we sum up the contributions from each character in the original string.

Time Complexity: O(26 * t + n), where n is the length of s and t is the number of transformations.
Space Complexity: O(1), as we use constant extra space regardless of input size.
"""

class Solution:
    def __init__(self, s: str, t: int) -> None:
        self.s = s
        self.t = t
        self.MOD = 10**9 + 7

    def total_characters(self) -> int:
        """Return the total number of characters after t transformations."""
        # If no transformations, return original string length
        if self.t == 0:
            return len(self.s) % self.MOD
        
        # Initialize previous array for 0 transformations
        # Each character contributes 1 at step 0
        prev = [1] * 26
        
        # Apply transformations t times
        for _ in range(self.t):
            curr = [0] * 26
            for c in range(26):
                if c < 25:
                    # Characters 'a' to 'y' transform to the next letter
                    curr[c] = prev[c + 1] % self.MOD
                else:
                    # 'z' transforms to 'a' and 'b', which are indices 0 and 1
                    curr[c] = (prev[0] + prev[1]) % self.MOD
            prev = curr
        
        # Calculate total characters after transformations
        total = 0
        for char in self.s:
            idx = ord(char) - ord('a')
            total = (total + prev[idx]) % self.MOD
        
        return total

# Test cases
solution1 = Solution("abc", 2)
print(f"Test 1: {solution1.total_characters()}")  # Expected: 3

solution2 = Solution("z", 2)
print(f"Test 2: {solution2.total_characters()}")  # Expected: 4

solution3 = Solution("jqktcurgdvlibczdsvnsg", 1)
print(f"Test 3: {solution3.total_characters()}")  # Expected: 21

solution4 = Solution("hello", 0)
print(f"Test 4: {solution4.total_characters()}")  # Expected: 5

solution5 = Solution("zzz", 3)
print(f"Test 5: {solution5.total_characters()}")  # Expected: 27 (3 z's × 9 characters each after 3 transformations)

solution6 = Solution("abcdefghijklmnopqrstuvwxyz", 1)
print(f"Test 6: {solution6.total_characters()}")  # Expected: 27 (26 characters + 1 extra from 'z')
