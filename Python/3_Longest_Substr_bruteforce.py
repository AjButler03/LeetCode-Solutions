# initial attempt; accidentally light on memory, but runtime is terrible

def test(s):
    dict = {} # dict for characters
    length = len(s)
    x = 0 # start of substr pointer
    y = 0 # pointer for char to look at
    maxLength = 0 # store maximum length of substring
    currLength = 0 # store current length of substring
    while x < length:
        while y < length:
            if s[y] in dict:
                dict = {}
                break
            dict[s[y]] = True
            y += 1
            currLength += 1
        x += 1 # increment substr start pointer
        y = x # set y to substr start pointer
        # update current length
        if currLength > maxLength:
            maxLength = currLength
        currLength = 0 # reset currLength
    return maxLength


# testing
test1 = "abcabcbb"
test2 = "bbbbb"
test3 = "pwwkew"
test4 = "dvdf"

print(test(test1)) # should be 3
print(test(test2)) # should be 1
print(test(test3)) # should be 3
print(test(test4)) # should be 3