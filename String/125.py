class Solution:
  def isPalindrome(self, s: str) -> bool:
    # 双向检测
    # s = "".join(i for i in s if i.isalpha() or i.isalnum()).lower()
    # index = 0
    # if len(s):
    #   while index <= len(s) / 2:
    #     if s[index] != s[- index - 1]:
    #       return False
    #     index += 1
    # return True

    # 翻转比较
    s = "".join(i for i in s if i.isalpha() or i.isalnum()).lower()
    s_reverse = s[::-1]
    return s == s_reverse


if __name__=="__main__":
  s = "race a car"
  method = Solution()
  answer = method.isPalindrome(s)
  print(answer)