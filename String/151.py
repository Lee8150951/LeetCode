class Solution:
  def reverseWords(self, s: str) -> str:
    sList = s.split()
    answer = ""
    for i in sList[::-1]:
      answer += i + " "
    return answer[0:-1]
    

if __name__=="__main__":
  s = "a good   example"
  method = Solution()
  answer = method.reverseWords(s)
  print(answer)