from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        length = len(nums)
        if length == 0:
            return 0
        answers = list()
        flag = 1
        for i in range(length - 1):
            first = nums[i]
            second = nums[i + 1]
            if second - first == 1:
                flag += 1
            else:
                answers.append(flag)
                flag = 1
        answers.append(flag)
        return max(answers)


if __name__=="__main__":
    nums = [1,2,0,1]
    method = Solution()
    answer = method.longestConsecutive(nums)
    print(answer)
    