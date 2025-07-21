"""
Problem: Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion (it is guaranteed that the answer is unique).

Example:
Input: s = "leeetcode"
Output: "leetcode"

Approach:
- Iterate through the string character by character.
- Keep track of the result so far.
- For each character, check if adding it would create three consecutive equal characters.
- If so, skip it (delete it). Otherwise, add it to the result.

Time Complexity: O(n) — single pass through the string
Space Complexity: O(n) — storing the result string
"""

class Solution:
    def __init__(self, s: str) -> None:
        self.s = s

    def make_fancy_string(self) -> str:
        """
        Delete minimum characters to ensure no three consecutive characters are equal.

        Returns:
            String with no three consecutive equal characters
        """
        if len(self.s) < 3:
            return self.s

        result = []

        for char in self.s:
            # Check if adding this character would create three consecutive equal chars
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                # Skip this character (delete it)
                continue
            else:
                # Safe to add this character
                result.append(char)

        return ''.join(result)

# Test cases
solution1 = Solution("leeetcode")
print(f"Test 1: {solution1.make_fancy_string()}")  # Expected: "leetcode"

solution2 = Solution("aaabaaaa")
print(f"Test 2: {solution2.make_fancy_string()}")  # Expected: "aabaa"

solution3 = Solution("aab")
print(f"Test 3: {solution3.make_fancy_string()}")  # Expected: "aab"

solution4 = Solution("aaaa")
print(f"Test 4: {solution4.make_fancy_string()}")  # Expected: "aa"

solution5 = Solution("abcdef")
print(f"Test 5: {solution5.make_fancy_string()}")  # Expected: "abcdef"

solution6 = Solution("a")
print(f"Test 6: {solution6.make_fancy_string()}")  # Expected: "a"

solution7 = Solution("")
print(f"Test 7: {solution7.make_fancy_string()}")  # Expected: ""
