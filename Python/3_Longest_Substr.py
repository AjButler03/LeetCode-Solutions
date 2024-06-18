# this is chatGPT generated; Once again, the AI is smarter than me
# (yes I know it's likely copying someone else's solution, and is not 'smarter'.)

def test(s):
    # Initialize pointers and the set for tracking characters
    left = 0
    right = 0
    max_length = 0
    char_set = set()
    
    while right < len(s):
        # If the character at 'right' is not in the set, add it and update max_length
        if s[right] not in char_set:
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            # If the character is in the set, remove the character at 'left' and move 'left' pointer
            char_set.remove(s[left])
            left += 1
    
    return max_length



# testing
test1 = "abcabcbb"
test2 = "bbbbb"
test3 = "pwwkew"
test4 = "dvdf"

print(test(test1)) # should be 3
print(test(test2)) # should be 1
print(test(test3)) # should be 3
print(test(test4)) # should be 3