from treeNode import TreeNode
from treeNode import creatBTree
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1

if __name__=="__main__":
    data = [1, 2, 2, 3, 2]
    root = creatBTree(data, 0)
    method = Solution()
    answer = method.maxDepth(root)
    print(answer)