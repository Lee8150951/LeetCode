from typing import List
class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
    answer, dictory = set(), dict()
    for num in nums:
      if num not in dictory:
        dictory[num] = 1
      else:
        dictory[num] += 1
      if dictory[num] > len(nums) / 3:
        answer.add(num)
    return list(answer)
      
if __name__=="__main__":
  nums = [1,1,1,3,3,2,2,2]
  method = Solution()
  answer = method.majorityElement(nums)
  print(answer)