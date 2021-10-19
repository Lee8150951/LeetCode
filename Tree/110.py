from treeNode import TreeNode
from treeNode import creatBTree
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

if __name__=="__main__":
    data = [1, 2, 2, 3, 2]
    root = creatBTree(data, 0)
    method = Solution()
    answer = method.isBalanced(root)
    print(answer)