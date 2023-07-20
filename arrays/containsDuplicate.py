class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        counted = set(nums)

        return len(nums) != len(counted)


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        num_dict = {}

        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = (i,)
            else:
                for j in num_dict[nums[i]]:
                    if abs(j - i) <= k:
                        return True
                num_dict[nums[i]] += (i,)

        return False
