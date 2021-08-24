from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 最终的列表
        answerRow = list()
        # i表示循环到的行数
        for i in range(numRows):
            # 当前循环到的行数字个数
            rowNum = i + 1
            # 初始化当前生成的列表
            currentRow = [1 for x in range(rowNum)]
            # 制作中间数字
            if i > 1:
                # j表示当前循环行的所到数字（从1到i - 1）
                for j in range(1, i):
                    leftNum = answerRow[i - 1][j - 1]
                    rightNum = answerRow[i - 1][j]
                    currentNum = leftNum + rightNum
                    currentRow[j] = currentNum
            # 将当前生成列表添加至最终列表表尾
            answerRow.append(currentRow)

        return answerRow


if __name__=="__main__":
  numRows = 10
  method = Solution()
  answer = method.generate(numRows)
  print(answer)