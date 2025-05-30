"""
Problem #2942: Find Words Containing Character

You are given a 0-indexed array of strings `words` and a character `x`.

Return an array of indices representing the words that contain the character `x`.

Note that the returned array may be in any order.

Example:
Input: words = ["leet","code","leetcode"], x = "e"
Output: [0,2]

Approach:
- Iterate through the words array with their indices.
- For each word, check if the character x is present in the word.
- If the character is found, add the current index to the result array.
- Return the array of indices.

Time Complexity: O(n*m) — where n is the number of words and m is the average length of words
Space Complexity: O(k) — where k is the number of words containing the character
"""

class Solution:

    def __init__(self, words: list[str], x: str) -> None:
        self.words = words
        self.x = x

    def find_words_containing(self) -> list[int]:
        """Return indices of words that contain the given character."""
        answer = []

        for i, word in enumerate(self.words):
            if self.x in word:
                answer.append(i)
        return answer

# Test cases
solution1 = Solution(["leet", "code", "leetcode"], "e")
print(f"Test 1: {solution1.find_words_containing()}")  # Expected: [0, 1, 2]

solution2 = Solution(["abc", "bcd", "aaaa", "cbc"], "a")
print(f"Test 2: {solution2.find_words_containing()}")  # Expected: [0, 2]

solution3 = Solution(["abc", "bcd", "aaaa", "cbc"], "z")
print(f"Test 3: {solution3.find_words_containing()}")  # Expected: []

solution4 = Solution(["hello", "world", "python"], "o")
print(f"Test 4: {solution4.find_words_containing()}")  # Expected: [0, 1, 2]

solution5 = Solution(["test"], "t")
print(f"Test 5: {solution5.find_words_containing()}")  # Expected: [0]
