
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'{self.data} -> {self.next}'
    def __str__(self):
        return stringify(self)

def stringify(node):
    s = ''
    while node is not None:
        value = node.data
        node = node.next
        s += str(value) + ' -> '
    return s + 'None'

def build(array):
    head = Node(array[0])
    probe = head
    for i in range(1, len(array)):
        probe.next = Node(array[i])
        probe = probe.next
    return head


def swap_pairs(head):
    if head is None or head.next is None:
        return head
    probe = head.next
    prev = head

    prev.next = swap_pairs(probe.next)
    probe.next = prev
    return probe



tst = build([1, 2, 3, 4, 5])
print('Original list')
print(swap_pairs(tst))