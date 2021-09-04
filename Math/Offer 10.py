class Solution:
  def fib(self, n: int) -> int:
    # 数组
    # fiboList = [0, 1]
    # for i in range(2, n + 1):
    #   fiboList.append(fiboList[i - 1] + fiboList[i - 2])
    # return fiboList[n] % 1000000007

    # 动态规划
    if n < 2:
      return n
    i, j, k = 0, 0, 1
    for i in range(2, n + 1):
      i, j = j, k
      k = i + j
    return k % 1000000007

if __name__=="__main__":
  n = 45
  method = Solution()
  answer = method.fib(n)
  print(answer)