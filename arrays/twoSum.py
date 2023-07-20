class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        table = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if str(diff) in table.keys():
                return table[str(diff)], i
            else:
                table[str(nums[i])] = i