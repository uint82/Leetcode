"""
Problem #409: Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, so "Aa" is not considered a palindrome here.

Examples:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Input: s = "a"
Output: 1

Input: s = "bb"
Output: 2

Approach:
- Count the occurrences of each character in the string.
- For each character:
  - If the count is even, all occurrences can be used in a palindrome.
  - If the count is odd, (count-1) occurrences can be used, with one possibly placed in the middle.
- Track if we have at least one character with an odd count, which can be placed in the middle.
- Calculate the total length based on these rules.

Time Complexity: O(n) — where n is the length of the string
Space Complexity: O(1) — at most 52 different characters (26 lowercase + 26 uppercase)
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Create a hashmap to count the occurrences of each character
        char_counts = {}
        
        # Count the occurrences of each character
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        length = 0
        has_odd = False
        
        # Calculate the length of the longest palindrome
        for count in char_counts.values():
            if count % 2 == 0:
                # If count is even, we can use all occurrences
                length += count
            else:
                # If count is odd, we can use (count-1) and mark that we have an odd count
                length += count - 1
                has_odd = True
        
        # If we have at least one character with odd count, we can place it in the middle
        if has_odd:
            length += 1
        
        return length

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("abccccdd"))  # Output: 7
    print(solution.longestPalindrome("a"))         # Output: 1
    print(solution.longestPalindrome("bb"))        # Output: 2
    print(solution.longestPalindrome("Aa"))        # Output: 1 (case-sensitive)
    print(solution.longestPalindrome("ccc"))       # Output: 3
    print(solution.longestPalindrome("bananas"))   # Output: 5 ("anana")
