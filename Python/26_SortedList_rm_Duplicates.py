# Suboptimal O(n^2) time
def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            # Check that not at the end of the list
            if i < length - 1:
                # Grab number at current position
                val = nums[i]
                # Grab number at i + 1
                val2 = nums[i + 1]
                # While there is list remaining and val2 == val, remove val2
                while i + 1 < length and val2 == val:
                    nums.pop(i + 1) # Remove duplicate
                    length -= 1
                    # Out of bounds check
                    if i + 1 < length:
                        val2 = nums[i + 1]
                    else:
                        break
        return length

# More optimal O(n) time
def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique] = nums[i]
                unique += 1
        return unique

# Even better Solution
def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        k = len(numset)

        i = 0  # list iter
        j = 0  # replace iter
        while numset:
            if nums[j] in numset:
                numset.remove(nums[j])
                nums[i] = nums[j]
                i += 1
            j += 1

        return k
    