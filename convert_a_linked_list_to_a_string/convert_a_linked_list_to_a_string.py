class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    s = ''
    while node is not None:
        value = node.data
        node = node.next
        s += str(value) + ' -> '
    return s + 'None'