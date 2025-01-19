"""
Linked Listが与えられてCycleがあるかを検出する問題

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

気を付けるところ
    入力がNoneの時にどう処理するか
    Raise Error
    Falseを返却

step 1
    考えられる解法
        1.
        setにNodeを保存していき、同じNodeがあればTrueを返す
        保存するのはNodeがユニークならNodeの値、ユニークではないなら、アドレス
        Cycleが無くても使用可能
        時間計算量は全てのNodeを訪れるためO(N), 空間計算量は全てのNodeを保存するためO(N)
        2.
        一個ずつ進むslowと二個ずつ進むfastを用意
        slowとfastが一致すればTrueを返す
        slowのnext pointerがNullの時はFalseを返す
        一致しないときは返却が無いので、必ずCycleがある場合のみに使用可能
        時間計算量は全てのNodeを訪れるためO(N), 空間計算量はslowとfastのNodeのみを保存すればいいので、O(1)

        最初のaccepted
        head.next is not None -> head.next:にして認知負荷を下げる
        elseで条件分岐しなくても、よさそう -> indentを減らせる
        毎回head.nextを条件にしているのは違和感がある
        curr_nodeをチェックしているので変数名を変えたほうがいい
        class Solution:
            def hasCycle(self, head: Optional[ListNode]) -> bool:
                if head is None:
                    return False

                visited_nodes = set()
                
                while head.next is not None:
                    if id(head) in visited_nodes:
                        return True
                    else:
                        visited_nodes.add(id(head))
                        head = head.next
                
                return False

        他の解法
        visited_nodeの中に訪れたnodeが入っていなければloopを継続
        もし、curr_nodeがNullならnodeが途切れているので、Falseを返す

        訪れたNodeを逆向きにしていくやり方
        Nodeを逆向きにしていってcurrent_nodeがheadと同じならTrue
        Time ComplexityがO(n), space complexityがO(1)
        破壊的変更がありなのかを確認してから実装したほうがよさそう

        フロイドの方法
        slowとfastを用意する

        try exepctで実装するとどんなエラーが起きるかを真面目に考える気が無いように見える
        動かせるか確認してから動かすコードのほうが見やすさがある


間違えたところ
    while head.next is Noneとしていた
    正しくはis not None条件はきちんと整理しておかないとエラーになる
    文章化しておきたい
    今回の場合なら、head.nextのポインターが存在するときにループを回すなので、is Noneとはならない
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        curr_node = head
        seen = set()
        while curr_node:
            if id(curr_node) in seen:
                return True
            seen.add(id(curr_node))
            curr_node = curr_node.next

        return False
    

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
    
        return False
    

class Solution_3:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None and head.next:
            return False
        
        curr_node = head
        prev = None
        while curr_node:
            temp_next = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = temp_next
            if curr_node == head:
                return True
        
        return False
        