from utils import ListNode
from utils import create_linked_list
class Solution:
  def getDecimalValue(self, head: ListNode) -> int:
    # 暴力解法
    cur = head
    string = ""
    while cur:
      string += str(cur.val)
      cur = cur.next
    return int(string, 2)
      

if __name__=="__main__":
  head = create_linked_list([1, 0, 1])
  method = Solution()
  answer = method.getDecimalValue(head)
  print(answer)