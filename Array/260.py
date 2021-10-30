from typing import List
class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    # 一次循环
    # hash = list()
    # for i in nums:
    #   if i not in hash:
    #     hash.append(i)
    #   elif i in hash:
    #     hash.remove(i)
    # return hash
      
if __name__=="__main__":
  nums = [0, 1]
  method = Solution()
  answer = method.singleNumber(nums)
  print(answer)