def longestPalindrome(s):
    # this was my initial attempt; it actually is a bit broken
    
    # Bruteforce solution, my intuition tells me that there should be a better way
    # The idea here is to essentially find all the palindromes, keeping the longest one
    p_start = 0 # Start idx for the palindrome
    p_end = 0 # End idx for palindrome
    s_length = len(s) # I don't want to type len(s) every time
    left = 0  
    right = s_length
    longest_palindrome = "" # to place the longest into
    # Itterate through all start points for palindromes
    while p_start < s_length:
        left = p_start
        right = s_length - 1
        p_end = right
        # Now figure out how long the palindrome from here is
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                right -= 1
                p_end = right
                
        # grab palindromic substr
        newpal =  s[(p_start):(p_end + 1)]
            
        # check if this palindrome is longer than existing longest
        if len(newpal) > len(longest_palindrome):
            longest_palindrome = newpal  
        p_start += 1 # Increment start point
        
    # return resulting longest palindrome
    return longest_palindrome
    
    
    
test1 = "babad"
test2 = "cbbd"
test3 = "aaaaaaaabbbbbbbbbbbbbbbbbbbbba"
test4 = "aacabdkacaa"
print("Result: " + longestPalindrome(test1))
print("Result: " + longestPalindrome(test2))
print("Result: " + longestPalindrome(test3))
print("Result: " + longestPalindrome(test4))