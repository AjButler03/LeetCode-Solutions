# ChatGPT generated solution; because I figured I'd study this idea to 
# see process, and hopefully learn from it

def test(nums1, nums2):
    # Ensure A is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        
        if i < m and nums2[j-1] > nums1[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0: max_of_left = nums2[j-1]
            elif j == 0: max_of_left = nums1[i-1]
            else: max_of_left = max(nums1[i-1], nums2[j-1])
            
            if (m + n) % 2 == 1:
                return max_of_left
            
            if i == m: min_of_right = nums2[j]
            elif j == n: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], nums2[j])
            
            return (max_of_left + min_of_right) / 2.0

# Example usage
test1 = [1, 3]
test2 = [2]
test3 = [1, 2]
test4 = [3, 4]
test5 = [1]
test6 = []

print(test(test1, test2))
print(test(test3, test4))
print(test(test5, test6))