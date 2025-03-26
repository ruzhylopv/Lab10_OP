class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def get_nth(node, index):
    probe = node
    count = 0
    while probe:
        if count == index:
            return probe
        count += 1
        probe = probe.next
    raise Exception()