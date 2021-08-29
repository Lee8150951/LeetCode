from typing import List
class Solution:
  def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    # 暴力解法（时间复杂度O(n^3)）
    # sum = 0
    # for i in range(len(arr)):
    #   # 检测剩余长度
    #   remainLength = len(arr) - i
    #   if remainLength % 2 == 0:
    #     remainLength -= 1
    #   for j in range(1, remainLength + 1, 2):
    #     for k in range(i, i + j):
    #       sum = sum + arr[k]
    # return sum

    # 使用列表和切片（时间复杂度O(n^2)）
    sumList = list()
    for i in range(len(arr)):
      count = summation = 0
      for j in arr[i:]:
        count += 1
        summation = summation + j
        sumList.append(summation)
        if count % 2 == 0:
          sumList.pop()
    return sum(sumList)
      
if __name__=="__main__":
  arr = [1, 4, 2, 5, 3]
  method = Solution()
  answer = method.sumOddLengthSubarrays(arr)
  print(answer)