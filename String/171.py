class Solution:
  def titleToNumber(self, columnTitle: str) -> int:
    index = len(columnTitle) - 1
    answer = 0
    while index >= 0:
      num = ord(columnTitle[index]) - 64
      answer = answer + num * (26 ** (len(columnTitle) - index - 1))
      index -= 1
    return answer

if __name__=="__main__":
  columnTitle = "FXSHRXW"
  method = Solution()
  answer = method.titleToNumber(columnTitle)
  print(answer)