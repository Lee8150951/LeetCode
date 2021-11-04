class Solution:
  def multiply(self, num1: str, num2: str) -> str:
    length = len(num2)
    answer = 0
    for i in num2:
      length -= 1
      current = int(num1) * int(i) * (10 ** length)
      answer += current
    return str(answer)

if __name__=="__main__":
  num1 = "1230"
  num2 = "123"
  method = Solution()
  answer = method.multiply(num1, num2)
  print(answer)