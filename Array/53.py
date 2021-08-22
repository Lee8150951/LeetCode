from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划法
        i = 1
        while i < len(nums):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
            i += 1
        return max(nums)
        # 贪心算法
        # preSum = maxSum = nums[0]
        # for i in range(1, len(nums)):
        #     preSum = max(nums[i], preSum + nums[i])
        #     maxSum = max(preSum, maxSum)
        # return maxSum
                

if __name__=="__main__":
  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  method = Solution()
  answer = method.maxSubArray(nums)
  print(answer)