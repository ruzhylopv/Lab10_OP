from stringify import stringify
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if head is None:
        return Node(data)
    if head.data > data:
        node = Node(data)
        node.next = head
        return node

    probe = head
    prev = head
    while probe is not None and probe.data < data:
        prev = probe
        probe = probe.next
    if probe is None:
        prev.next = Node(data)
    else:
        val = Node(data)
        prev.next = val
        val.next = probe 
    return head
    # Your code goes here.
    # Make sure to return the head of the list.