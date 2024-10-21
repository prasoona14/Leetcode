"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        new_hashmap={}
        curr = head

        if not head:
            return None
            
        while curr:
            copy = Node(curr.val)
            new_hashmap[curr] = copy
            curr=curr.next

        curr=head
        while curr:
            if curr.next:
                new_hashmap[curr].next = new_hashmap[curr.next]
            if curr.random:
                new_hashmap[curr].random = new_hashmap[curr.random]
            curr=curr.next
        
        return new_hashmap[head]
