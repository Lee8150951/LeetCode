class Solution:
  # 暴力解法（超时）
  # def myPow(self, x: float, n: int) -> float:
  #   answer = 1
  #   for _ in range(abs(n)):
  #       answer *= x
  #   if n > 0:
  #     return answer
  #   else:
  #     return 1 / answer
  def myPow(self, x: float, n: int) -> float:
    def quickMul(N):
      ans = 1.0
      x_contribute = x
      while N > 0:
        if N % 2 == 1:
          ans *= x_contribute
        x_contribute *= x_contribute
        N //= 2
      return ans
    
    return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


if __name__=="__main__":
  x = 2.00000
  n = 0
  method = Solution()
  answer = method.myPow(x, n)
  print(answer)