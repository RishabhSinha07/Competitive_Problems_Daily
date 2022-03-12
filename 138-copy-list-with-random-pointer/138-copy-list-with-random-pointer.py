"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Thought process: 

We can easily solve this problem with linear time and linear space using a hash map. But we want to reduce the time
complexity. 

To do that we will create the following changes. 
1. We will create a new copy of the LL. And while doing so we will point the random pointer of each new node to
the original node. 
2. After processing the original node, we will move to the next node and point the node next to new node
3. We will apply this logic to each new node : node.random = node.random.random.next

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        NewNode = Result = Node(0)
        
        while head:
            NewNode.next = Node(head.val,head.next,head)
            temp = head.next
            head.next = NewNode.next
            head = temp
            NewNode=NewNode.next
        
        temp = Result.next
        while temp:
            try:
                temp.random = temp.random.random.next
            except:
                temp.random = None
            temp = temp.next
        
        return Result.next