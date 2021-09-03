class Solution:
  def reverseVowels(self, s: str) -> str:
    # 双指针
    left, right = 0, len(s) - 1
    vowelList = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    s = [i for i in s]
    while left < right:
      if s[left] in vowelList:
        while right >= 0:
          if s[right] in vowelList:
            s[left], s[right] = s[right], s[left]
            right -= 1
            break
          right -= 1
      left += 1
    return "".join(s)


if __name__=="__main__":
  s = "Marge, let's \"went.\" I await news telegram."
  method = Solution()
  answer = method.reverseVowels(s)
  print(answer)