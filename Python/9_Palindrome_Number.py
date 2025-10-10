# Idea: Have index pointers for left and right, moving inward until one of two things happen:
#   1: left and right indexes are next to one another or equal to one another (return true)
#   2: the number at left/right idx does not match (return false)

def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        intstr = str(x)
        left = 0
        right = len(intstr) - 1
        
        # Itterate until left/right pointers are the same or next to each other
        while right - left > 1:
            if intstr[left] == intstr[right]:
                left += 1
                right -= 1
            else:
                return False
        
        # Check for even numbered palindrome
        if left != right and intstr[left] != intstr[right]:
            return False
        else:
            return True
        
        
# Alternative solution that is a bit simpler
# Create string, reverse it, then see if they are the same.
def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        intstr = str(x)
        rev_intstr = ""
        for i in intstr:
            rev_intstr = i + rev_intstr
        if (rev_intstr==intstr):
            return True
        else:
            return False