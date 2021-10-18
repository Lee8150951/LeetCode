from treeNode import TreeNode
from treeNode import creatBTree
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


if __name__=="__main__":
    data = [1, 2, 2, 3]
    root = creatBTree(data, 0)
    method = Solution()
    answer = method.postorderTraversal(root)
    print(answer)