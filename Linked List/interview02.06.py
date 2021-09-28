from utils import ListNode
from utils import create_linked_list
class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    cur = head
    array = list()
    while cur:
      array.append(cur.val)
      cur = cur.next
    return array == array[::-1]

if __name__=="__main__":
  head = create_linked_list([1, 2, 2, 1])
  method = Solution()
  answer = method.isPalindrome(head)
  print(answer)