from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        listLength = len(nums)
        fast = slow = 1
        while fast < listLength:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__=="__main__":
  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
  method = Solution()
  answer = method.removeDuplicates(nums)
  print(answer)