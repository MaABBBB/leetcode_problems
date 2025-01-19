"""
Linked Listが与えられてcycleが始まったNodeを返却する問題

解法
step1.
    1.
    フロイドの解法
    slowとfastを用意する
    解法がいまいち思いつかないから調べる
    Time ComplexityがO(N), Space ComplexityがO(1)
    2.
    全てのNodeをseenに入れていき、seenに入っていたらcycleの始まりとみなしNodeを返却する
    Tiem complextiyがO(N), Space complexityがO(N)
    一番最初に思いつくやり方
    3.
    破壊的変更がOKな場合
    一度訪れたNodeに訪問済みのMarkerを入れる
    Time complexityがO(N), Space complexityがO(1)

    とりあえず全部実装してみる

解いてからの感想
    fastとslowに再代入せずに新しくfrom_startやfrom_slowなど別の変数名を与えたほうがわかりやすい
    また、関数化したほうがよさそう
    内部でしか使わない関数としてわかりやすい
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        current = head

        while current:
            if current in seen:
                return current
            seen.add(current)
            current = current.next

        return None
    
class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current:
            if current.val is None:
                return current
            current.val = None
            current = current.next
        return None
    

class Solution3:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_colision_node(head) -> ListNode | None:
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return fast
                
            return None

        colision_node = find_colision_node(head)
        if colision_node is None:
            return None
        
        restart_node = head
        while restart_node:
            if restart_node == colision_node:
                return restart_node
            restart_node = restart_node.next
            colision_node = colision_node.next
        return None