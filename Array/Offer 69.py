from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # maxNum = max(arr)
        # return arr.index(maxNum)

        # if arr[-1] > arr[-2]:
        #     return len(arr) - 1
        # for i in range(len(arr) - 1):
        #     if arr[i] > arr[i + 1]:
        #         return i

        # 二分查找
        n = len(arr)
        left, right, ans = 1, n - 2, 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


if __name__=="__main__":
  arr = [1, 2, 3]
  method = Solution()
  answer = method.peakIndexInMountainArray(arr)
  print(answer)