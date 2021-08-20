from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return left


if __name__=="__main__":
  nums = [1, 3]
  target = 2
  method = Solution()
  answer = method.searchInsert(nums, target)
  print(answer)