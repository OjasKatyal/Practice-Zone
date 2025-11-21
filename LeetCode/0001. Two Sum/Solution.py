#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            comp = target - num

            if comp in seen:
                return [seen[comp], index]

            seen[num] = index


# @lc code=end

