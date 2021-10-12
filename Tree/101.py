from treeNode import TreeNode
from treeNode import creatBTree
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(left, right):
            if not left and not right:
                return True
            elif (not left and right) or (left and not right):
                return False
            else:
                return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
        return check(root, root)

if __name__=="__main__":
    data = [1,2,2,3,4,4,3]
    root = creatBTree(data, 0)
    method = Solution()
    answer = method.isSymmetric(root)
    print(answer)