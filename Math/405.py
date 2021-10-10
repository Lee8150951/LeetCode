CONV = "0123456789abcdef"
class Solution:
  def toHex(self, num: int) -> str:
    ans = []
    # 32位2进制数，转换成16进制 -> 4个一组，一共八组
    for _ in range(8):
      ans.append(num%16)
      num //= 16
      if not num:
        break
    return "".join(CONV[n] for n in ans[::-1])

if __name__=="__main__":
  num = 26
  method = Solution()
  answer = method.toHex(num)
  print(answer)