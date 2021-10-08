from treeNode import TreeNode
from treeNode import creatBTree
from typing import List
class Solution:
    # 迭代法
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

if __name__=="__main__":
    data = [1, 2, 2, 3]
    root = creatBTree(data, 0)
    method = Solution()
    answer = method.preorderTraversal(root)
    print(answer)