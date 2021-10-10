from treeNode import TreeNode
from treeNode import creatBTree
from typing import List
class Solution:
    # 错误，例如[1, 1]和[1, null, 1]
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     def traversal(root: TreeNode) -> List[int]:
    #         if not root:
    #             return []
    #         return traversal(root.left) + [root.val] + traversal(root.right)
    #     return traversal(p) == traversal(q)

    # 深度优先
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        elif not p or not q: return False
        elif p.val != q.val: return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__=="__main__":
    p = creatBTree([1, 2, 3], 0)
    q = creatBTree([1, 2, 3], 0)
    method = Solution()
    answer = method.isSameTree(p, q)
    print(answer)