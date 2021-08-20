from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        fast = slow = 0
        while fast < length:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__=="__main__":
  nums = [3, 2, 2, 3]
  val = 3
  method = Solution()
  answer = method.removeElement(nums, val)
  print(answer)