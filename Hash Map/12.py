class Solution:
  def intToRoman(self, num: int) -> str:
    dictory = {
      1000 : "M", 900 : "CM", 500 : "D", 400 : "CD",
      100 : "C", 90 : "XC", 50 : "L", 40 : "XL",
      10 : "X", 9 : "IX", 5 : "V", 4 : "IV", 1 : "I"
    }
    answer = ""
    for key, value in dictory.items():
      while num >= key:
        num -= key
        answer += value
      if num == 0:
        break
    return answer

    

if __name__=="__main__":
  num = 58
  method = Solution()
  answer = method.intToRoman(num)
  print(answer)