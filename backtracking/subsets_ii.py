class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, curr):
            result.append(curr[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                backtrack(i + 1, curr)

                curr.pop()

        nums.sort()
        result = []
        backtrack(0, [])

        return result
