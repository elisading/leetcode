class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if idx >= len(candidates) or total > target:
                return

            curr.append(candidates[idx])
            # decision including candidate
            backtrack(idx, curr, total + candidates[idx])

            curr.pop()
            # decision not including candidate
            backtrack(idx + 1, curr, total)

        result = []
        backtrack(0, [], 0)
        return result
