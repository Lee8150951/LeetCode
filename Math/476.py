class Solution:
  def findComplement(self, num: int) -> int:
    numString = str(bin(num))
    numString = numString[2:]
    answer = ""
    for i in numString:
      if i == "0":
        answer += "1"
      else:
        answer += "0"
    return int(answer, 2)

if __name__=="__main__":
  num = 5
  method = Solution()
  answer = method.findComplement(num)
  print(answer)