from typing import List
from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 先排序后两两置零
        # nums.sort()
        # length = len(nums)
        # fast = 1
        # slow = 0
        # if length == 1:
        #     return nums[0]
        # while fast < length:
        #     if nums[fast] == nums[slow]:
        #         nums[fast] = nums[slow] = 0
        #     fast += 1
        #     slow += 1
        # nums.sort()
        # if nums[0] != 0:
        #     return nums[0]
        # else:
        #    return nums[length - 1] 

        # 位运算
        return reduce(lambda x, y: x ^ y, nums)

if __name__=="__main__":
  nums = [-1,-1,-2]
  method = Solution()
  answer = method.singleNumber(nums)
  print(answer)