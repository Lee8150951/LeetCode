from typing import List
class Solution:
  def isSelfCrossing(self, distance: List[int]) -> bool:
    n = len(distance)
    # 处理第 1 种情况
    i = 0
    while i < n and (i < 2 or distance[i] > distance[i - 2]):
      i += 1
    if i == n:
      return False
    # 处理第 j 次移动的情况
    if ((i == 3 and distance[i] == distance[i - 2])
        or (i >= 4 and distance[i] >= distance[i - 2] - distance[i - 4])):
      distance[i - 1] -= distance[i - 3]
    i += 1
    # 处理第 2 种情况
    while i < n and distance[i] < distance[i - 2]:
      i += 1
    return i != n

if __name__=="__main__":
  distance = [1, 2, 3, 4]
  method = Solution()
  answer = method.isSelfCrossing(distance)
  print(answer)