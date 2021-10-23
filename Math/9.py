class Solution:
  def isPalindrome(self, x: int) -> bool:
    # 双指针
    string = str(x)
    length = len(string) // 2
    for i in range(length):
      if string[i] != string[-i - 1]:
        return False
    return True


if __name__=="__main__":
  x = 101
  method = Solution()
  answer = method.isPalindrome(x)
  print(answer)