from utils import TreeNode
from utils import listCreatTree
from typing import List
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

if __name__=="__main__":
    data = [1, 2, 2, 3, 2]
    root = listCreatTree(None, data, 0)
    method = Solution()
    answer = method.inorderTraversal(root)
    print(answer)