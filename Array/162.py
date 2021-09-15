from typing import List
class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    # 一次遍历寻找峰值
    nums.append(nums[-1] - 1)
    nums.insert(0, nums[0] - 1)
    for i in range(1, len(nums) - 1):
      if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        return i - 1


if __name__=="__main__":
  nums = [2]
  method = Solution()
  answer = method.findPeakElement(nums)
  print(answer)