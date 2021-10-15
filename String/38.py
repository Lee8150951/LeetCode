class Solution:
  # 检测字符串
  def checkString(self, s: str) -> str:
    s += "0"
    ansString = ""
    current = [1, 0]
    for i in s:
      if current[1] == i:
        current[0] += 1
      else:
        ansString += str(current[0]) + str(current[1])
        current = [1, 0]
        current[1] = i
    return ansString[2:]

  def countAndSay(self, n: int) -> str:
    ans = "1"
    if n == 1:
      return ans
    for _ in range(n - 1):
      ans = self.checkString(ans)
    return ans

if __name__=="__main__":
  n = 2
  method = Solution()
  answer = method.countAndSay(n)
  print(answer)