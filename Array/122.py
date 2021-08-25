from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思路：寻找低点，只要在升就不停
        # 一旦降就更新低点并计算上一个小高峰差值
        # 第一个值存储上一个最高或最低，第二个值存储当前最高或最低值
        prices.append(0)
        minPrice = maxPrice = prices[0]
        sum = 0
        for i in range(len(prices)):
            if prices[i] < prices[i - 1]:
                maxPrice = prices[i - 1]
                sum = sum + maxPrice - minPrice
                minPrice = prices[i]
        return sum


if __name__=="__main__":
  prices = [6,1,3,2,4,7]

  method = Solution()
  answer = method.maxProfit(prices)
  print(answer)