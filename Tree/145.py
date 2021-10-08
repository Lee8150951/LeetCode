from treeNode import TreeNode
from treeNode import creatBTree
from typing import List
class Solution:
    # 迭代法
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

if __name__=="__main__":
    data = [1, 2, 2, 3]
    root = creatBTree(data, 0)
    method = Solution()
    answer = method.postorderTraversal(root)
    print(answer)