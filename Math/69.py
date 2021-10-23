class Solution:
  def mySqrt(self, x: int) -> int:
    if x == 0: return 0
    ans, other = 1, x
    while ans < other:
      ans += 1
      other = x // ans
    return other

if __name__=="__main__":
  x = 0
  method = Solution()
  answer = method.mySqrt(x)
  print(answer)