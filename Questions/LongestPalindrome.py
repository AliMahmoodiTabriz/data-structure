def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest_palindrome = ""
    
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)
        longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)
    
    return longest_palindrome

# Test
print(longestPalindrome("babad"))  # "bab" veya "aba"
print(longestPalindrome("cbbd"))   # "bb"
print(longestPalindrome("cccccc")) # "cccccc"

print(longestPalindrome("cccccc"))
