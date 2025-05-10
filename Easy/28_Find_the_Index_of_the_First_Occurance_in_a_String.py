"""
Problem #28: Find the Index of the First Occurrence in a String (KMP Algorithm)

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

KMP Approach:
- The Knuth-Morris-Pratt (KMP) algorithm improves string matching by using information about the pattern itself.
- First, build a "partial match" table (also called the "failure function" or "LPS" - Longest Prefix Suffix) for the needle.
- This table helps skip characters we know will match based on pattern repetitions, avoiding redundant comparisons.
- Then search the haystack using this table, achieving linear time complexity.

Key benefits of KMP:
- Never backtracks in the haystack string
- Skips comparisons by leveraging pattern information
- Achieves O(m + n) time complexity instead of O(m * n)

Time Complexity: O(m + n) where m is the length of haystack and n is the length of needle
Space Complexity: O(n) for storing the LPS array
"""

class Solution:
    def __init__(self, haystack: str, needle: str) -> None:
        self.haystack = haystack
        self.needle = needle
    
    def _build_lps_array(self) -> list[int]:
        """
        Build the LPS (Longest Prefix Suffix) array for the needle pattern.
        
        LPS[i] contains the length of the longest proper prefix of needle[0...i]
        which is also a suffix of needle[0...i].
        """
        n = len(self.needle)
        lps = [0] * n  # Initialize LPS array with zeros
        
        # Length of the previous longest prefix & suffix
        length = 0
        i = 1
        
        # Calculate LPS[i] for i = 1 to n-1
        while i < n:
            if self.needle[i] == self.needle[length]:
                # Found matching character, update length and LPS
                length += 1
                lps[i] = length
                i += 1
            else:
                # Characters don't match
                if length != 0:
                    # Adjust length using previous value in LPS
                    # This is key insight of KMP - we don't start from 0
                    length = lps[length - 1]
                else:
                    # No matching prefix, set LPS[i] = 0 and move forward
                    lps[i] = 0
                    i += 1
        
        return lps
    
    def str_str(self) -> int:
        """
        Return the index of the first occurrence of needle in haystack using KMP algorithm,
        or -1 if not found.
        """
        # Edge cases
        if not self.needle:
            return 0  # Empty needle is always found at index 0
        
        if not self.haystack:
            return -1 if self.needle else 0
        
        m = len(self.haystack)
        n = len(self.needle)
        
        # If needle is longer than haystack, it can't be found
        if n > m:
            return -1
        
        # Build the LPS array for pattern matching
        lps = self._build_lps_array()
        
        # Pointers for haystack and needle
        i = 0  # Index for haystack
        j = 0  # Index for needle
        
        while i < m:
            # Current characters match, move both pointers
            if self.needle[j] == self.haystack[i]:
                i += 1
                j += 1
            
            # If we've matched the entire needle, we found it!
            if j == n:
                return i - j  # Return the starting index
            
            # Mismatch after j matches
            elif i < m and self.needle[j] != self.haystack[i]:
                if j != 0:
                    # Use LPS to skip comparisons we know will match
                    j = lps[j - 1]
                else:
                    # No matching prefix, move to next character in haystack
                    i += 1
        
        # If we get here, no match was found
        return -1

# Test cases
solution1 = Solution("sadbutsad", "sad")
print(f"Test 1: {solution1.str_str()}")  # Expected: 0

solution2 = Solution("leetcode", "leeto")
print(f"Test 2: {solution2.str_str()}")  # Expected: -1

solution3 = Solution("hello", "ll")
print(f"Test 3: {solution3.str_str()}")  # Expected: 2

solution4 = Solution("mississippi", "issip")
print(f"Test 4: {solution4.str_str()}")  # Expected: 4

solution5 = Solution("aaa", "aaaa")
print(f"Test 5: {solution5.str_str()}")  # Expected: -1

solution6 = Solution("", "")
print(f"Test 6: {solution6.str_str()}")  # Expected: 0

solution7 = Solution("ababcaababcaabc", "ababcaabc")
print(f"Test 7: {solution7.str_str()}")  # Expected: 6 - Good KMP test case with pattern repetition

solution8 = Solution("aabaaabaaac", "aabaaac")
print(f"Test 8: {solution8.str_str()}")  # Expected: 3 - Another good KMP test case
