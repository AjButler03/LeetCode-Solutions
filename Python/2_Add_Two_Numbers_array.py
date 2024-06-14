# This is what I initially tried to do; I had assumed that since the linked-
# lists were presented as arrays in the example, that was just how they were
# implemented. That was not case. I'll keep this here for shits and gigs, tho.

# converts an array arr of length len of integers to a full number,
# where the array represents that number with the digits stored in reverse order.
def arrToNum(len, arr):
    num = 0 # define variable to store converted number
    for x in range(len):
        y = len - x - 1 # figure out index of digit
        num = num + (arr[y] * 10 ** y) # add digit to fullnum
    return num

# converts a number into an array where the digits are stored in reverse order.
def numToArr(num):
    arr = [] # establish empty arr
    # extract each digit
    while (num >= 10):
        digit = num % 10 # extract digit
        arr.append(digit) # add digit to arr
        num = num // 10 # remove digit from num
    arr.append(num) # add the remaining digit to arr
    return arr


# basic idea
l1 = [2, 4, 3]
l2 = [5, 6, 4]

num1 = arrToNum(len(l1), l1)
num2 = arrToNum(len(l2), l2)

sum = num1 + num2

print(numToArr(sum))