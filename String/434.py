class Solution:
  def countSegments(self, s: str) -> int:
    # answerList = s.split(" ")
    # ans = len(answerList)
    # for i in range(len(answerList)):
    #   if answerList[i] == "":
    #     ans -= 1
    # return ans

    return len(s.split())

if __name__=="__main__":
  s = ""
  method = Solution()
  answer = method.countSegments(s)
  print(answer)