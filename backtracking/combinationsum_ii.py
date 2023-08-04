class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, curr, total):
            if total == target:
                result.append(curr.copy())
            if total > target:
                return

            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue

                curr.append(candidates[i])
                # decision including candidate
                backtrack(i + 1, curr, total + candidates[i])

                curr.pop()
                prev = candidates[i]

        candidates.sort()
        result = []
        backtrack(0, [], 0)
        return result
