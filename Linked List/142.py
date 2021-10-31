from utils import ListNode
from utils import create_linked_list
class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    # 哈希表
    hash = set()
    point = head
    while point:
      if point in hash:
        flag = point
        break
      hash.add(point)
      point = point.next
    while head:
      if head == point:
        return head
      head = head.next
    return None


if __name__=="__main__":
  head = [3,2,0,-4]
  method = Solution()
  answer = method.detectCycle(head)
  print(answer)