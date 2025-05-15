"""
Problem #2900: Longest Unequal Adjacent Groups Subsequence I

You are given two arrays of strings, words and groups, of the same length n.
The groups array indicates the group each word in words belongs to (0 or 1).

A subsequence of indices of words is called valid if the corresponding groups 
of adjacent indices have different values.

Return a valid subsequence of words with the maximum possible length.
If there are multiple subsequences with the maximum length, return any of them.

Example:
Input: words = ["a","b","c","d"], groups = [1,0,1,1]
Output: ["a","b","c"]

Approach:
- Start with the first word and its group
- For each subsequent word, check if its group is different from the last included word's group
- If different, include this word in the result and update the current group
- This greedy approach works because we only care about adjacent groups being different

Time Complexity: O(n) — single pass through the arrays
Space Complexity: O(n) — in the worst case, all words could be included in the result
"""

class Solution:

    def __init__(self, words: list[str], groups: list[int]) -> None:
        self.words = words
        self.groups = groups

    def get_longest_subsequence(self) -> list[str]:
        """Return the longest subsequence of words where adjacent groups are different."""
        n = len(self.words)
        
        if n == 0:
            return []

        result = [self.words[0]]
        current_group = self.groups[0]

        for i in range(1, n):
            if self.groups[i] != current_group:
                result.append(self.words[i])
                current_group = self.groups[i]
        return result


# Test cases
solution1 = Solution(["a", "b", "c", "d"], [1, 0, 1, 1])
print(f"Test 1: {solution1.get_longest_subsequence()}")  # Expected: ["a", "b", "c"]

solution2 = Solution(["hello", "world", "leetcode"], [1, 1, 0])
print(f"Test 2: {solution2.get_longest_subsequence()}")  # Expected: ["hello", "leetcode"]

solution3 = Solution(["aa", "bb", "cc", "dd", "ee"], [0, 1, 0, 1, 0])
print(f"Test 3: {solution3.get_longest_subsequence()}")  # Expected: ["aa", "bb", "cc", "dd", "ee"]

solution4 = Solution(["a", "b", "c", "d"], [0, 0, 0, 0])
print(f"Test 4: {solution4.get_longest_subsequence()}")  # Expected: ["a"]
