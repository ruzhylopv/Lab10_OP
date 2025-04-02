class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return stringify(self)
    def __repr__(self):
        return f'{self.data} -> {self.next}'

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


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head.next:
        raise ValueError()
    first = head
    second = head.next
    second_head = second
    

    while first and second:
        if first.next:
            first.next = first.next.next
        if second.next:
            second.next = second.next.next
        first = first.next
        second = second.next
    return Context(head, second_head)

print('Initial list:')
tst = build([1])
print(tst)
print('Testing alternating split:')
context = alternating_split(tst)
print('Testing first:')
print(context.first)
print('Testing second:')
print(context.second)