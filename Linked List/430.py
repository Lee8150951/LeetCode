from utils import ListNode
from utils import create_linked_list
class Solution:
  def flatten(self, head: "Node") -> "Node":
    def dfs(node: "Node") -> "Node":
      cur = node
      # 记录链表的最后一个节点
      last = None
      while cur:
        nxt = cur.next
        # 如果有子节点，那么首先处理子节点
        if cur.child:
          child_last = dfs(cur.child)
          
          nxt = cur.next
          # 将 node 与 child 相连
          cur.next = cur.child
          cur.child.prev = cur
          # 如果 nxt 不为空，就将 last 与 nxt 相连
          if nxt:
            child_last.next = nxt
            nxt.prev = child_last
          # 将 child 置为空
          cur.child = None
          last = child_last
        else:
          last = cur
        cur = nxt
      return last
    dfs(head)
    return head


if __name__=="__main__":
  head = create_linked_list([1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12])
  method = Solution()
  answer = method.flatten(head)
  print(answer)