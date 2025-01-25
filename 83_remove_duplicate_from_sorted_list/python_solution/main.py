"""
ソート済みのlinked listが与えられるので、重複した要素をひとつにする
step1
    setを用意して、今の要素がsetの中にあればnextをする
    この場合、currentがseenの中にあるかを確認 -> あればseenの中に無い要素が出てくるまでnextを繰り返す
    1. nextがseenの中にあるかをチェック
    2. なければcurrent = current.nextとする
    3. あれば、seenの中にないところまでnext.nextとする
        3a. current.next = next
        3b. current = current.nextとする
    Time ComplexityがO(n), Space ComplexityがO(n)

    Spaceを1にする方法はないか?
    currentの値を保存する変数
    currentとnextが同じか確認
    同じならnextを一つ先に進める
    currentとnextが異なる場合、currentをnextにする
    Spaceが1になる

    currentを使うときはprevのような比較をする
    比較をしないならnodeなどがよさそう
"""

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        current = head

        while current and current.next:
            seen.add(current.val)
            next = current.next
            while next and next.val in seen:
                next = next.next
            current.next = next
            current = current.next
        
        return head

    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current:
            curr_val = current.val
            next = current.next
            while next and next.val == curr_val:
                next = next.next
            current.next = next
            current = current.next
        return head
    
    def deleteDuplicates3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head