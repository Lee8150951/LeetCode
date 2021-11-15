from math import sqrt
class Solution:
  def bulbSwitch(self, n: int) -> int:
    return int(sqrt(n + 0.5))

if __name__=="__main__":
  n = 6
  method = Solution()
  answer = method.bulbSwitch(n)
  print(answer)