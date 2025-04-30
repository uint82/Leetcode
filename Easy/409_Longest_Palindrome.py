class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Returns the length of the longest palindrome that can be built with letters from s.
        
        Args:
            s: A string consisting of lowercase and/or uppercase English letters
            
        Returns:
            Length of the longest possible palindrome
        """
        
        # Time Complexity: O(n), where n is the length of the string s.
        #   - Building the frequency map takes O(n) as we iterate through the string once.
        #   - Processing the frequency map takes O(1) since it stores at most 52 characters (26 lowercase + 26 uppercase).
        # Space Complexity: O(1), since the frequency map stores at most 52 characters, which is constant regardless of input size.
        
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