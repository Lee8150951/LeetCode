from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 超时
        # length = len(prices)
        # spreadList = list()
        # for index, price in enumerate(prices):
        #     for i in range(index, length):
        #         spreadList.append(prices[i] - price)
        # return max(spreadList)
        # 动态规划
        minPrice = prices[0]
        maxSpread = 0
        for i in prices:
            # 记录上一个最小值今天的最大利润
            maxSpread = max(maxSpread, i - minPrice)
            # 记录上一个获得的最小值
            minPrice = min(minPrice, i)
        return maxSpread


if __name__=="__main__":
  prices = [7, 1, 5, 3, 6, 4]
  method = Solution()
  answer = method.maxProfit(prices)
  print(answer)