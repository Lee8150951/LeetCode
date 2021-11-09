from typing import List
class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    roundList = list()
    # 通过获取的matrix来计算外围序列
    def readRound():
      # 第一行
      if matrix:
        if matrix[0]:
          for i in matrix[0]: roundList.append(i)
          del matrix[0]
      # 最右侧一列
      if matrix:
        if matrix[0]:
          height_01 = len(matrix)
          for i in range(height_01):
            roundList.append(matrix[i][-1])
            del matrix[i][-1]
      # 最后一行
      if matrix:
        if matrix[0]:
          for i in matrix[-1][::-1]: roundList.append(i)
          del matrix[-1]
      # 最左一列
      if matrix:
        if matrix[0]:
          height_02 = len(matrix)
          for i in range(height_02):
            roundList.append(matrix[height_02 - i - 1][0])
            del matrix[height_02 - i - 1][0]
    while matrix and matrix[0]:
      readRound()
    return roundList

if __name__=="__main__":
  matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
  method = Solution()
  answer = method.spiralOrder(matrix)
  print(answer)