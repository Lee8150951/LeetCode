#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
# 方法一：暴力解法
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         lens = len(nums)
#         for i in range(lens):
#             for j in range(i+1, lens):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []
# 方法二：Hash表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Table = dict()
        numsList = enumerate(nums)
        for i, num in numsList:
            if target - num in Table:
                return [Table[target - num], i]
            Table[num] = i
# @lc code=end
