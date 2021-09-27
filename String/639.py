class Solution:
  def numDecodings(self, s: str) -> int:
    # 检查一个字符
    def checkOneChar(ch: str) -> int:
      if ch == "0":
        return 0
      else:
        return 9 if ch == "*" else 1
    
    # 检查两个字符
    def checkTwoChar(ch0: str, ch1: str) -> int:
      if ch0 == ch1 == "*":
        return 15
      elif ch0 == "*":
        return 2 if ch1 <= "6" else 1
      elif ch1 == "*":
        return 9 if ch0 == "1" else (6 if ch0 == "2" else 0)
      return int(ch0 != "0" and int(ch0) * 10 + int(ch1) <= 26)

    length = len(s)
    a, b, c = 0, 1, 0
    for i in range(1, length + 1):
      c = b * checkOneChar(s[i - 1])
      if i > 1:
        c += a * checkTwoChar(s[i - 2], s[i - 1])
      c %= 10 ** 9 + 7
      a = b
      b = c
    return c

if __name__=="__main__":
  s = "2*"
  method = Solution()
  answer = method.numDecodings(s)
  print(answer)