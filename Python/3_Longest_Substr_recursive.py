# second attempt; try recurisve solution
# incomplete for now; I'll come back to this at some point

def test(s):
    length = len(s)
    # base case; longest substr of 
    # str with length 1 is 1
    if length == 1:
        return # length? substr? TBD
    
    



# testing
test1 = "abcabcbb"
test2 = "bbbbb"
test3 = "pwwkew"
test4 = "dvdf"

print(test(test1)) # should be 3
print(test(test2)) # should be 1
print(test(test3)) # should be 3
print(test(test4)) # should be 3