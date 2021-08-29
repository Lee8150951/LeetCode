from typing import List
class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:  
    # 一次遍历
    # answerList = list()
    # count = 0
    # for i in range(len(nums)):
    #   if i + 1 != len(nums):
    #     if nums[i + 1] - nums[i] == 1:
    #       count += 1
    #     else:
    #       if nums[i] - count != nums[i]:
    #         answer = str(nums[i] - count) + "->" + str(nums[i])
    #       else:
    #         answer = str(nums[i])
    #       answerList.append(answer)
    #       count = 0
    #   else:
    #     if nums[i] - nums[i - 1] == 1:
    #       answer = str(nums[i] - count) + "->" + str(nums[i])
    #     else:
    #       answer = str(nums[i])
    #     answerList.append(answer)

    # return answerList

    # 尾部添加数字
    nums.append(2 ** 32)
    ret, start = [], 0
    for i in range(1,len(nums)):
      if nums[i] - nums[i - 1] > 1:
        if i - 1 == start:
          ret.append(str(nums[start]))
        else:
          ret.append(f"{nums[start]}->{nums[i - 1]}")
        start = i
    return ret

      
if __name__=="__main__":
  nums = [0,2,3,4,6,8,9]
  method = Solution()
  answer = method.summaryRanges(nums)
  print(answer)