"""
linked listが回文になっているかを判定する問題

stackに入れていき、同じ値が来たら取り出す?
どちらもO(n)になる

スタックの先頭と別の値が入ってきたら取り出しを開始する
取り出した値とnodeの値が異なればfalseを返す
nodeが最後まできたらtrueを返す

単純な文字列の比較でもいい
listに値を全て入れて、そのリストをひっくり返して同じかをチェック

わざわざ半分から判定しなくても、listにすべての値を入れてからlistを双方向で探索すればよかった

follow up問題としてO(n), O(1)で解いてみる
連結リストの問題で、O(1) spaceを見たときに、別途メモリーを使うことができないので
ポインター操作が必要との方向で考えるのはほぼ間違いありません。

回文の判定には二つのパターンがある
中心から両端に向かって走査
    リストが奇数か偶数かで対応が変わる
両端から中心に向かって走査

今回の場合
    中心を探して、pointerの向きを変える
    中心からなら前半部分
    両端からなら後半部分
    まずはlinked listの中心を探す
    次に後半部分のlistを反転させる
    最後に両端から走査する

    双方向連結リストなら両端から走査すればいい話
    単方向なら両端か中心のどちらからスタート
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_values = []
        current = head

        while current:
            node_values.append(current.val)
            current = current.next

        left_pointer = 0
        right_pointer = len(node_values) -1
    
        while left_pointer <= right_pointer:
            print(left_pointer, right_pointer)
            if node_values[left_pointer] != node_values[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True
    
    def isPalindrome_2(self, head: Optional[ListNode]) -> bool:
        """
        この問題でカバーされているテクニック
        ・フロイドのウサギと亀のアルゴリズム
        ・連結リストのはんてん
        ・ダミーノードでエッジケースの対応
            prev = Noneとしたところ
        """
        # まずは中心を探す
        # フロイドのアルゴリズムを使用して、中心を探す
        current = head
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # この時点でslowが中心になっている
        # slowから先のリストを反転させる
        current = slow
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        left = head
        right = prev

        while right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True