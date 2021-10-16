from treeNode import TreeNode
from typing import List
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)
         

if __name__=="__main__":
    nums = [1, 2, 2, 3, 2, 3, 4, 5, 1, 3, 4, 5, 3, 4, 5, 6, 7]
    method = Solution()
    answer = method.sortedArrayToBST(nums)
    print(answer)