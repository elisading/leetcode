class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > max_water:
                max_water = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water
