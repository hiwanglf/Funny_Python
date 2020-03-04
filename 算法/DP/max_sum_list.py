# https://leetcode-cn.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dict_map = {}

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)+1):
                if sum(nums[i:j]) not in dict_map:
                    dict_map[sum(nums[i:j])] = nums[i:j]

        return max(dict_map.keys())
