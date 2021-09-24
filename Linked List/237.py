from utils import ListNode
from utils import create_linked_list
class Solution:
  def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next

if __name__=="__main__":
  node = create_linked_list([4, 5, 1, 9])
  node = 5
  method = Solution()
  answer = method.deleteNode(node)
  print(answer)