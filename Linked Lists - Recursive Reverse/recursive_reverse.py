def stringify(node):
    s = ''
    while node is not None:
        value = node.data
        node = node.next
        s += str(value) + ' -> '
    return s + 'None'


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return stringify(self)
    def __repr__(self):
        return f'{self.data} -> {self.next}'

def reverse(head):
    if head is None or head.next is None:
        return head
    reversed_head = reverse(head.next) #діюча reversed_head: 3 -> None, head: 2 -> 3 -> None. 2 X 3; 3 -> 2
    head.next.next = head # 3 -> 2
    head.next = None # 2 X 3
    return reversed_head

    # your code goes here
