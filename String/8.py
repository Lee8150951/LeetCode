class Solution(object):
  def myAtoi(self, s):
    s = s.lstrip()
    if not s:
      return 0
    sign = -1 if s[0] == "-" else 1
    if sign == -1 or s[0] == "+":
      s = s[1:]
    d = 0
    for i in s:
      if i.isdigit():
        d *= 10
        d += ord(i) - 48
      else:
        break
    return max(-2**31, min(sign * d,2**31-1))

if __name__=="__main__":
  s = "-42 bsba"
  method = Solution()
  answer = method.myAtoi(s)
  print(answer)