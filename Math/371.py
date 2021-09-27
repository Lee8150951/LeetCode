class Solution:
  def getSum(self, a: int, b: int) -> int:
    return sum([a, b])

if __name__=="__main__":
  a = 1
  b = 2
  method = Solution()
  answer = method.getSum(a, b)
  print(answer)