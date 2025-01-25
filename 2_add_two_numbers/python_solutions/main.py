"""
二つの空ではないlinked listが与えられる、0以上の整数のみ
stackを二つ用意して全部のnodeの値をいれて取り出しながら計算するのを思いつく

Time Complexity O(n), space O(n)

spaceのほうをどうにかしてO(1)に抑えたい

nodeを二回行き来してもいいなら順番を逆にしてもう一度計算すればよさそう
二回触るのが美しくない気がする
(stackに入れるのとやっていることは同じか?)

とりあえずstakとnodeを二回触る方法で解いてみる

問題を読み間違えていた
302は2 -> 0 -> 3として受け取る

そのうえでもう一度考える

l1, l2, 桁上げが存在すればloopを回す
1. l1があれば桁上げとl1の値を足し、l2があればl1の値に足す
2. divmod(今回の値, 10)で商とあまりを出し、余りを次のloopに渡す

最初の桁上げは0

再帰で書いてみる
再帰が全く書けないので、再帰について資料探して読む

Pythonのビルトイン関数知らない者が多すぎるのでちょこちょこ読んでいく
"""


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(val=0)
        current = root

        carry = 0
        total_value = 0
        while l1 or l2 or carry:
            if l1:
                total_value += l1.val
                l1 = l1.next
            if l2:
                total_value += l2.val
                l2 = l2.next
            carry, val = divmod(total_value, 10)
            total_value = carry

            current.next = ListNode(val=val)
            current = current.next

        return root.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2:
            total = l1.val + l2.val
            if total >= 10:
                node = ListNode(val=total)
                node.next = self.addTwoNumbers(l1=l1.next, l2=l2.next)
                return node
            else:

