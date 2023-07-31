class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            k = (l + r)//2
            hours = 0

            for p in piles:
                hours += (p + k - 1)//k

            if hours > h:
                l = k + 1

            else:
                r = k

        return r
