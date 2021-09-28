from typing import Counter
from utils import ListNode
from utils import create_linked_list
class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    cur, pre = head, None
    while cur:
      tmp = cur.next # 暂存后继节点 cur.next
      cur.next = pre # 修改 next 引用指向
      pre = cur      # pre 暂存 cur
      cur = tmp      # cur 访问下一节点
    return pre

if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 4, 5, None])
  method = Solution()
  answer = method.reverseList(head)
  print(answer)