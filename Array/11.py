from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 暴力解法（超时）
        # answer = 0
        # for index_left, length_left in enumerate(height):
        #     for index_right, length_right in enumerate(height):
        #         length = min(length_left, length_right)
        #         width = index_right - index_left
        #         answer = max(answer, length * width)
        # return answer

        # 双指针
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
    

if __name__=="__main__":
    height = [4,3,2,1,4]
    method = Solution()
    answer = method.maxArea(height)
    print(answer)