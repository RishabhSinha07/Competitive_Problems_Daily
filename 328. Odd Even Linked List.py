# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.


# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    Node = head
    counter = 0
    temp = thead = ListNode()

    if Node is None:
        return None

    while Node:
        if counter % 2 == 0:
            prev = Node
            Node = Node.next
            counter += 1
        else:
            prev.next = Node.next
            temp.next = ListNode(Node.val)
            temp = temp.next
            Node = Node.next
            counter += 1
    prev.next = thead.next
    return head


if __name__ == "__main__":
    Node = ListNode(1)
    Node.next = ListNode(2)
    Node = Node.next
    Node.next = ListNode(3)
    Node = Node.next
    Node.next = ListNode(4)
    Node = Node.next
    print(oddEvenList(Node))


# Runtime: 40 ms, faster than 92.04% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 15.8 MB, less than 29.93% of Python3 online submissions for Odd Even Linked List.
