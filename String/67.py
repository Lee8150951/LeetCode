class Solution:
  def addBinary(self, a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    answer = bin(a + b)
    return answer[2:]

if __name__=="__main__":
  a = "11"
  b = "1"
  method = Solution()
  answer = method.addBinary(a, b)
  print(answer)