class Node(object):
    def __repr__(self):
        return f'{self.data} -> {self.next}'
    def __init__(self, data):
        self.data = data
        self.next = None

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


tst = build([1, 2, 3, 3, 3, 4, 5])

def remove_duplicates(head):
    
    probe = head
    prev = probe
    while probe:
        # prev = probe.next
        probe = probe.next
        if probe and prev.data == probe.data:
            prev.next = probe.next
        else:
            prev = probe
        # prev = probe
    return head

print(stringify(remove_duplicates(tst)))