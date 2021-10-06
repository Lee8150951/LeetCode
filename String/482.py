class Solution:
  def licenseKeyFormatting(self, s: str, k: int) -> str:
    string = s.split("-")
    newString = ""
    for i in string:
      newString += i
    newString = newString.upper()
    answer = ""
    nums = [k for _ in range(len(newString) // k)]
    nums.insert(0, len(newString) % k)
    for num in nums:
      answer += newString[0:num]
      answer += "-"
      newString = newString[num:]
    answer = answer[0:len(answer) - 1]
    if len(answer) == 0:
      return answer
    if answer[0] == "-":
      answer = answer[1:]
    return answer



if __name__=="__main__":
  s = "---"
  k = 3
  method = Solution()
  answer = method.licenseKeyFormatting(s, k)
  print(answer)