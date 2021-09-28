from utils import ListNode
from utils import create_linked_list
class Solution:
  def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next


if __name__=="__main__":
  node = 8
  method = Solution()
  answer = method.deleteNode(node)
  print(answer)