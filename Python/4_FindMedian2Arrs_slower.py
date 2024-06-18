# If I am given two sorted lists, it should be fairly trivial to combine the two into one larger sorted list. 
# From there, just find the 'middle' element. Simple if len is odd, still relatively easy if len is even.
# in this implementation, the runtime is O(m+n). This is slower than the requested O(log(m+n)).

def test(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    p1 = 0 # idx pointer for nums1
    p2 = 0 # idx pointer for nums2
    allNums = [] # array for nums1 + nums2
    
    # combine sorted arrays
    while (p1 < len1) and (p2 < len2):
        if nums1[p1] <= nums2[p2]:
            allNums.append(nums1[p1]) # add number from nums1
            p1 += 1 # increment p1
        elif nums1[p1] > nums2[p2]:
            allNums.append(nums2[p2]) # add number from nums2
            p2 += 1 # increment p2
            
    # add any remaining elements
    if p1 >= len1:
        # add remaining elements from p2
        while p2 < len2:
            allNums.append(nums2[p2])
            p2 += 1
    else:
        # add remaining elements from p1
        while p1 < len1:
            allNums.append(nums1[p1])
            p1 += 1
        
    # find middle (median) element; first check if odd or even length
    len3 = len(allNums)
    if len3 % 2 > 0:
        # odd length
        return allNums[len3 // 2] # return middle element
    else:
        # even length; return mean of middle two numbers
        x = allNums[(len3 // 2) - 1]
        y = allNums[len3 // 2]
        return (x + y) / 2
            
            
test1 = [1, 3]
test2 = [2]
test3 = [1, 2]
test4 = [3, 4]

print(test(test1, test2))
print(test(test3, test4))