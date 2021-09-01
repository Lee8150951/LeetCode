class Solution:
  def convertToTitle(self, columnNumber: int) -> str:
    ans = list()
    while columnNumber > 0:
      columnNumber -= 1
      ans.append(chr(columnNumber % 26 + ord("A")))
      columnNumber //= 26
    return "".join(ans[::-1])


if __name__=="__main__":
  columnNumber = 52
  method = Solution()
  answer = method.convertToTitle(columnNumber)
  print(answer)