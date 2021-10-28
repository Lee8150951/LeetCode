from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 暴力解法（超时）
        # answer = list()
        # first = 0
        # while first < len(nums):
        #     second = first + 1
        #     while second < len(nums):
        #         third = second + 1
        #         while third < len(nums):
        #             if nums[first] + nums[second] + nums[third] == 0:
        #                 target = sorted([nums[first], nums[second], nums[third]])
        #                 if target not in answer:
        #                     answer.append(target)
        #             third += 1
        #         second += 1
        #     first += 1
        # return answer

        # 暴力解法（超时）
        # answer = list()
        # first = 0
        # while first < len(nums):
        #     second = first + 1
        #     while second < len(nums):
        #         p = 0 - nums[first] - nums[second]
        #         if p in nums[second + 1:]:
        #             target = sorted([nums[first], nums[second], p])
        #             if target not in answer:
        #                 answer.append(target)
        #         second += 1
        #     first += 1
        # return answer

        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res

if __name__=="__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    method = Solution()
    answer = method.threeSum(nums)
    print(answer)