"""
ListNodeが与えられて重複があるNodeを削除する

step1
    現在のnodeと次のnodeが同じなら違う値になるまでnodeを動かし、違う値のnodeをheadに入れる
    どちらもO(1)
    prevの考え方がでなくて答えを見た

step2
    答えを見て見つけた解法
    prevを使う
    1. 現在のnodeと次のnodeが異なる値になるまで進める
    2. prev.nextが現在のnodeと同じなら1で重複がなかった事が保証されているので分岐
        a. 同じの場合
            prevとcurrentを次に進める
        b. 違う場合
            prev.nextをcurrent.nextにする
            currentを次に進める

    3. 最後にdummy_node.nextを返却し、終了
        a. headは何も変わっていないがhead以降のnodeのnextが変わっている可能性があるので、dummy_node.nextを返す

    
    異なるならprev.nextを現在のnodeの次のnode

    prevを使わない方法もあるらしい
    番兵アルゴリズムとか
    is_deleted変数を使った方法
    よくわからんかった
    https://docs.python.org/3/library/itertools.html#itertools.groupby
    この辺はじめてしった

    自然言語で説明可能な方法で書いていったほうが人に説明できる
    この書き換えは意識する
while A:
    if B:
        break
    ....

while A and not B:
    ....
"""


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(val="dummy")
        dummy_node.next = head

        current = dummy_node.next
        previous = dummy_node

        while current:
            while current.next and current.val == current.next.val:
                current = current.next

            if previous.next is current:
                previous = previous.next
                current = current.next
            else:
                previous.next = current.next
                current = current.next
        return dummy_node.next

    def deleteDuplicates_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(val=-1)
        dummy_node.next = head
        current = dummy_node.next
        prev = dummy_node

        while current:
            while current.next and current.val == current.next.val:
                current = current.next
            
            if prev.next == current:
                prev = prev.next
                current = current.next
            else:
                prev.next = current.next
                current = current.next
        return dummy_node.next
    
    def deleteDuplicates_3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        while loopを一回だけで実装してみる
        重複していたかをis_duplicatedに保存すればよさそう
        """

        dummy = ListNode(val=-1000)
        dummy.next = head
        current = head
        prev = dummy


        while current:
            print(f"current_val: {current.val}")
            if current.next is None:
                return dummy.next

            if current.val == current.next.val:
                current = current.next
                continue

            if prev.next == current:
                prev = prev.next
                current = current.next
            else:
                prev.next = current.next
                current = current.next
        
        return dummy.next
    
    def deleteDuplicates_4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        whileの中でif文を使って現在のprev.next == currentをしないようにするにはcurrentを重複がないところまで運ぶ必要がある
        """
        def _skip_node(head, skip_value):
            while head and head.val == skip_value:
                head = head.next
            return head

        sentinel = ListNode()
        sentinel.next = None
        cursor = head
        last_unique_node = sentinel

        while cursor:
            print(cursor.val)
            if cursor.next and cursor.val == cursor.next.val:
                cursor = _skip_node(cursor, cursor.val)
                continue

            last_unique_node.next = cursor
            last_unique_node = last_unique_node.next
            cursor = cursor.next
        # last_unique_node.nextをNoneにしていなくてエラー
        # 全パターンを考慮できていない気がする
        # 今回だったら 1, 1, 2 1, 2 ,2 1, 1, 2, 2みたいな感じで樹形図で書き出せばよかった
        # 1が続く、続かない、続くならさらに続く場合、続かない場合、みたいな感じ 
        return sentinel.next