from typing import List
from heapq import heappush, heappop, nlargest
class Solution:
  # 超时
  # def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
  #   k = min(k, len(profits))
  #   pairs = list(zip(profits, capital))
  #   for i in range(k):
  #     if w >= min(capital):
  #       profitList = []
  #       for pair in pairs:
  #         if pair[1] <= w:
  #           profitList.append(pair)
  #       maxProfit = max([i[0] for i in profitList])
  #       del pairs[profits.index(maxProfit)]
  #       del capital[profits.index(maxProfit)]
  #       profits.remove(maxProfit)
  #       w += maxProfit
  #   return w

  # 堆排序
  def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    if w >= max(capital):
      return w + sum(nlargest(k, profits))
    n = len(profits)
    curr = 0
    arr = [(capital[i], profits[i]) for i in range(n)]
    arr.sort(key = lambda x : x[0])
    pq = []
    for _ in range(k):
      while curr < n and arr[curr][0] <= w:
        heappush(pq, -arr[curr][1])
        curr += 1
      if pq:
        w -= heappop(pq)
      else:
        break
    return w

if __name__=="__main__":
  k = 2
  w = 0
  profits = [1, 2, 3]
  capital = [0, 1, 1]
  method = Solution()
  answer = method.findMaximizedCapital(k, w, profits, capital)
  print(answer)