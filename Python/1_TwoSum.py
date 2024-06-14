class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create dictionary (hashmap) for numbers' indicies
        Dict = {}
        for i, num in enumerate(nums):
            # y = complement
            y = target - num
            # check if complement y is in dictionary
            if (y in Dict):
                # if yes, return indecies of num and complement
                return [Dict[y], i]
            # if no, add x to dictionary and continue
            Dict[num] = i