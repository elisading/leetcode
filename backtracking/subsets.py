class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, curr):
            # curr larger than input
            if start == len(nums):
                result.append(curr[:])
                return

            # include curr
            curr.append(nums[start])
            backtrack(start + 1, curr)

            # exclude curr
            curr.pop()
            backtrack(start + 1, curr)

        result = []

        backtrack(0, [])

        return result
