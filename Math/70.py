class Solution:
  def climbStairs(self, n: int) -> int:
    cur_01, cur_02 = 1, 1
    if n == 1 or n == 0:
      return n
    for i in range(n - 1):
      cur_03 = cur_01 + cur_02
      cur_01 = cur_02
      cur_02 = cur_03
    return cur_03

if __name__=="__main__":
  n = 6
  method = Solution()
  answer = method.climbStairs(n)
  print(answer)