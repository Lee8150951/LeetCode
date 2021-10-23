from typing import List
class Solution:
  def constructRectangle(self, area: int) -> List[int]:
    length = int(area ** 0.5)
    while area % length != 0:
      length -= 1
    return [area // length, length]

if __name__=="__main__":
  area = 2
  method = Solution()
  answer = method.constructRectangle(area)
  print(answer)