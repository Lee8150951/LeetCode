from typing import List
class Solution:
  def numberOfBoomerangs(self, points: List[List[int]]) -> int:
    # 哈希表
    count = 0
    for point_01 in points:
      distanceTable = dict()
      for point_02 in points:
        distance = (point_01[0] - point_02[0]) ** 2 + (point_01[1] - point_02[1]) ** 2
        if distance not in distanceTable:
          distanceTable[distance] = 1
        else:
          distanceTable[distance] += 1
      for i in distanceTable.values():
        count += i * (i - 1)
    return count
      

if __name__=="__main__":
  points = [[1,1],[2,2],[3,3]]
  method = Solution()
  answer = method.numberOfBoomerangs(points)
  print(answer)