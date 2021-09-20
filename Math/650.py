class Solution:
  def minSteps(self, n: int) -> int:
    count = 0
    if n == 1:
      return 0
    while n > 1:
      if n % 2 == 0:
        count += 2
        n //= 2
      else:
        flag = n
        for i in range(n // 2, 2, -1):
          if n % i == 0:
            time = n // i
            count += time
            n = i
            break
        if flag == n:
          count += n
          break
    return count


if __name__=="__main__":
  n = 9
  method = Solution()
  answer = method.minSteps(n)
  print(answer)