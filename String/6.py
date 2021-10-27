class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if len(s) <= numRows or numRows == 1:
      return s
    answer = ""
    # 获取每行的头并存入列表
    charList = [i for i in s[:numRows]]
    # 每个Z型回文长度
    length = numRows * 2 - 2
    # 补足长度形成完整Z型字符串
    gap = length - (len(s) - numRows) % length
    s += gap * "0"
    s = s[numRows:]
    # 每length个字符进行一次处理
    times = len(s) // length
    for i in range(times):
      # 获取当前Z型尾部字符串
      currentString = s[i * length: i * length + length]
      # 获取回文中心点，并向两周扩散
      point = numRows - 2
      # 添加头尾
      charList[0] += currentString[point]
      charList[-1] += currentString[-1]
      # 循环次数
      for j in range(1, point + 1):
        left = currentString[point - j]
        right = currentString[point + j]
        charList[j] += left + right
    for chars in charList:
      for char in chars:
        if not char.isnumeric():
          answer += char
    return answer


if __name__=="__main__":
  s = "PAYPALISHIRING"
  numRows = 5
  method = Solution()
  answer = method.convert(s, numRows)
  print(answer)