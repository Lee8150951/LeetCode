from typing import List
class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    ansMatrix = [[] for _ in range(len(matrix))]
    for column in matrix[::-1]:
      for index, num in enumerate(column):
        ansMatrix[index].append(num)
    for i in range(len(matrix)):
      matrix[i] = ansMatrix[i]

if __name__=="__main__":
  matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
  method = Solution()
  answer = method.rotate(matrix)
  print(answer)