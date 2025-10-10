# 10/09/2025
# Idea: Idx pointers for left/right, itterate inward one step at a time based on which line is shorter.
# Record the maximum volume, updating as new maximum found
# Stop when idx pointers for left/right are the same, return max
def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        left = 0
        right = len(height) - 1
        
        while left != right:
            # Grab container wall heights
            l_height = height[left]
            r_height = height[right]
            
            h = min(l_height, r_height) # Container height
            w = right - left # Container width
            vol = h * w # Calculate volume
            # Update max_vol if necessary
            if vol > max_vol:
                max_vol = vol
            # Determine which side is shorter, move in from there
            if r_height < l_height:
                right -= 1
            else:
                left += 1
        
        return max_vol
    
# This is basically the same code as above, just slightly optimized
def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        l = 0
        r = len(height) - 1
        
        while l != r:
            new_vol = min(height[l], height[r]) * (r - l)
            max_vol = max(max_vol, new_vol)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
                
        return max_vol
            