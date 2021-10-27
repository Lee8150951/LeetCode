# class Solution:
#   def longestPalindrome(self, s: str) -> str:
#     # 中心拓展并返回长度
#     def centerExpansion(length: int, position: int, s: str) -> str:
#       if length == 1:
#         return s
#       ans = str(s[position])
#       times = min(position, length - position - 1)
#       for i in range(times):
#         left = s[position - i - 1]
#         right = s[position + i + 1]
#         if left == right:
#           ans = str(left) + ans + str(right)
#         else:
#           if left == s[position]:
#             ans = str(left) + ans
#             break
#           elif right == s[position]:
#             ans = ans + str(right)
#             break
#           else:
#             break
#       return ans

#     length = len(s)
#     answer = ""
#     maxLength = 0
#     answers = list()
#     for i in range(1, length):
#       current = centerExpansion(length, i, s)
#       print(current)
#       maxLength = max(maxLength, len(current))
#       if maxLength == len(current): answer = current
#       answers.append(current)
#     print(answers)
#     return answer

class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


if __name__=="__main__":
  s = "b"
  method = Solution()
  answer = method.longestPalindrome(s)
  print(answer)