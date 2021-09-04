from collections import Counter
class Solution:
  def longestPalindrome(self, s: str) -> int:
    table = dict(Counter(s))
    answer = 0
    for i in table.values():
      if i % 2 == 0:
        answer += i
      else:
        answer += i - 1
    if any(i % 2 == 1 for i in table.values()):
      answer += 1
    return answer


if __name__=="__main__":
  s = "ccc"
  method = Solution()
  answer = method.longestPalindrome(s)
  print(answer)