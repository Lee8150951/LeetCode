class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    i = len(s) - 1
    answer = list()
    while i >= 0:
      if s[i] != " ":
        answer.append(s[i])
      elif s[i] == " " and answer:
        break
      i -= 1
    return len(answer)


if __name__=="__main__":
  s = "luffy is still joyboy"
  method = Solution()
  answer = method.lengthOfLastWord(s)
  print(answer)