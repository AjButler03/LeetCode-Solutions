def longestPalindrome(s):
    # more betterer solution; expand outward from center
    
    if not s:
        return ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest_palindrome = ""
    
    for i in range(len(s)):
        # Odd length palindrome (single middle character)
        palindrome1 = expand_around_center(i, i)
        # Even length palindrome (2 'middle' characters)
        palindrome2 = expand_around_center(i, i + 1)

        # Choose the longest palindrome
        longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)

    return longest_palindrome
    
    
    
test1 = "babad"
test2 = "cbbd"
test3 = "aaaaaaaabbbbbbbbbbbbbbbbbbbbba"
test4 = "aacabdkacaa"
print("Result: " + longestPalindrome(test1))
print("Result: " + longestPalindrome(test2))
print("Result: " + longestPalindrome(test3))
print("Result: " + longestPalindrome(test4))