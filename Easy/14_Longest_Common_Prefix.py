"""
Problem #14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Examples:
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Approach:
- Handle edge cases first:
  - If the array is empty, return an empty string.
  - If there's only one string, return that string as the prefix.
- Find the length of the shortest string to avoid index errors.
- Iterate through the characters of the first string up to the shortest length.
- For each position, compare the character in the first string with the character 
  at the same position in all other strings.
- If a mismatch is found, return the prefix up to that position.
- If no mismatch is found, return the prefix up to the length of the shortest string.

Time Complexity: O(S) — where S is the sum of all characters in all strings
Space Complexity: O(1) — only using a constant amount of extra space
"""

class Solution:

    def __init__(self, strs: list[str]) -> None:
        self.strs = strs

    def longestCommonPrefix(self) -> str:

        # local variable
        strs = self.strs

        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        paling_pendek = min(len(s) for s in strs)

        for i in range(paling_pendek):
            current = strs[0][i]

            for word in strs[1:]:
                if current != word[i]:
                    return strs[0][:i]
        
        return strs[0][:paling_pendek]
    
# test
# Basic test cases
test1 = Solution(["flower", "flow", "flight"])
print(f"Test 1: ['flower', 'flow', 'flight'] should be 'fl': {test1.longestCommonPrefix()}")  # Should return "fl"

test2 = Solution(["dog", "racecar", "car"])
print(f"Test 2: ['dog', 'racecar', 'car'] should be '': {test2.longestCommonPrefix()}")  # Should return "" (no common prefix)

test3 = Solution(["interspecies", "interstellar", "interstate"])
print(f"Test 3: ['interspecies', 'interstellar', 'interstate'] should be 'inter': {test3.longestCommonPrefix()}")  # Should return "inter"

test4 = Solution(["prefix", "preface", "preamble"])
print(f"Test 4: ['prefix', 'preface', 'preamble'] should be 'pre': {test4.longestCommonPrefix()}")  # Should return "pre"

test5 = Solution(["abc", "abcd", "abcde"])
print(f"Test 5: ['abc', 'abcd', 'abcde'] should be 'abc': {test5.longestCommonPrefix()}")  # Should return "abc"

# Edge cases
test6 = Solution([""])
print(f"Test 6: [''] should be '': {test6.longestCommonPrefix()}")  # Should return "" (single empty string)

test7 = Solution([])
print(f"Test 7: [] should be '': {test7.longestCommonPrefix()}")  # Should return "" (empty array)

test8 = Solution(["single"])
print(f"Test 8: ['single'] should be 'single': {test8.longestCommonPrefix()}")  # Should return "single" (single string)

test9 = Solution(["a", "b", "c"])
print(f"Test 9: ['a', 'b', 'c'] should be '': {test9.longestCommonPrefix()}")  # Should return "" (no common prefix)

# Common prefix cases
test10 = Solution(["aaa", "aaaa", "aaaaa"])
print(f"Test 10: ['aaa', 'aaaa', 'aaaaa'] should be 'aaa': {test10.longestCommonPrefix()}")  # Should return "aaa"

test11 = Solution(["abc", "abc", "abc"])
print(f"Test 11: ['abc', 'abc', 'abc'] should be 'abc': {test11.longestCommonPrefix()}")  # Should return "abc" (identical strings)

test12 = Solution(["", "test", "testing"])
print(f"Test 12: ['', 'test', 'testing'] should be '': {test12.longestCommonPrefix()}")  # Should return "" (empty string in list)

test13 = Solution(["test", "test", "test"])
print(f"Test 13: ['test', 'test', 'test'] should be 'test': {test13.longestCommonPrefix()}")  # Should return "test" (identical strings)

# Complex cases
test14 = Solution(["international", "interface", "interact", "internal"])
print(f"Test 14: ['international', 'interface', 'interact', 'internal'] should be 'inter: {test14.longestCommonPrefix()}")  # Should return "inte"

test15 = Solution(["python", "pyth", "py", "pythonic"])
print(f"Test 15: ['python', 'pyth', 'py', 'pythonic'] should be 'py': {test15.longestCommonPrefix()}")  # Should return "py"
