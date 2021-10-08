class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# 根据列表创建二叉树
def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == '#':
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)
        pNode.right = creatBTree(data, 2 * index + 2)
    return pNode