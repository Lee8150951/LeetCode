from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        answer = [intervals[0]]
        for i in intervals:
            if i[0] <= answer[-1][1]:
                answer[-1][1] = max(i[1], answer[-1][1])
            else:
                answer.append(i)
        return answer
    

if __name__=="__main__":
  intervals = [[1,4],[2,3]]
  method = Solution()
  answer = method.merge(intervals)
  print(answer)