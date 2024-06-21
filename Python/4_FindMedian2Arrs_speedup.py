# the idea with this updated version is to find the kth largest element- so, similar to the simple combine lists version,
# we iterate through both lists, but we only go to the kth and k+1th element.
# if even number of nums, return (kth + k+1th) /2.
# if odd number of nums, return kth.
# side note: this code seems really messy given what it's supposed to be doing. But, if it works, it works.
# Not a sigificant speedup; still O(m+n), but in theory it's checking half the numbers that the previous solution was.

def test(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    p1 = len1 - 1 # idx pointer for nums1
    p2 = len2 - 1 # idx pointer for nums2
    current = len1 + len2 # used to store what order of largest number the code is on
    kth = 0 # used to store kth largest element when found
    k1th = 0 # used to store k+1th largest element when found
    target = (len1 + len2) // 2 # kth element
    
    
    print("target k =", target)
    # iterate through arrays
    while (current >= target) and (p1 >= 0) and (p2 >= 0):
        if nums1[p1] >= nums2[p2]:
            # num in nums1 is larger
            k = nums1[p1]
            p1 -= 1 # decrement p1
        elif nums1[p1] < nums2[p2]:
            # num in nums2 is larger
            k = nums2[p2]
            p2 -= 1 # decrement p2
        # check if kth or k+1th; if so, store
        if (current == target + 1):
            kth = k
        elif (current == target):
            k1th = k
        current -= 1 # decrement current

    # if we still haven't gotten to the k+1th element, need to iterate through whatever is left
    # so, check which array has been iterated through completely, iterate the other one
    if current >= target: # check to ignore this if already found kth and k+1th
        if p2 < 0:
            # nums2 is already iterated through completely; check nums1
            while (current >= target):
                k = nums1[p1]
                p1 -= 1 # decrement p1
                # check if kth or k+1th; if so, store
                if (current == target + 1):
                    kth = k
                elif (current == target):
                    k1th = k
                current -= 1 # decrement current
        else:
            # nums1 is already iterated through completely; check nums2
            while (current >= target):
                k = nums2[p2]
                p2 -= 1 # decrement p2
                # check if kth or k+1th; if so, store
                if (current == target + 1):
                    kth = k
                elif (current == target):
                    k1th = k
                current -= 1 # decrement current
    # check if even or odd number of nums, return median accordingly
    if (len1 + len2) % 2 == 0:
        return (kth + k1th) / 2 # even number of nums
    else:
        return kth # odd number of nums
     
test1 = [1, 3]
test2 = [2]
test3 = [1, 2]
test4 = [3, 4]
test5 = [1]
test6 = []

print(test(test1, test2))
print(test(test3, test4))
print(test(test5, test6))