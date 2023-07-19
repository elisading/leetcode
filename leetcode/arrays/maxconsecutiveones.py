class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts = []
        temp = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                counts.append(temp)
                temp = 0

        counts.append(temp)

        return max(counts)
