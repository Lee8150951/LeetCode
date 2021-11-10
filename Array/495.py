from typing import List
class Solution:
    # 暴力解法（超时）
    # def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    #     if duration == 0:
    #         return 0
    #     timeSet = set(timeSeries)
    #     for i in timeSeries:
    #         for j in range(duration):
    #             timeSet.add(i + j)
    #     return len(timeSet)
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans, expired = 0, 0
        for i in range(len(timeSeries)):
            if timeSeries[i] >= expired:
                ans += duration
            else:
                ans += timeSeries[i] + duration - expired
            expired = timeSeries[i] + duration
        return ans
        

if __name__=="__main__":
    timeSeries = [1, 4]
    duration = 2
    method = Solution()
    answer = method.findPoisonedDuration(timeSeries, duration)
    print(answer)