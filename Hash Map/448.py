from typing import List
class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    # 超时
    # answer = list()
    # for i in range(1, len(nums) + 1):
    #   if i not in set(nums):
    #     answer.append(i)
    # return answer

    return list(set(range(1, len(nums) + 1)).difference(set(nums)))


if __name__=="__main__":
  nums = [1,1]
  method = Solution()
  answer = method.findDisappearedNumbers(nums)
  print(answer)