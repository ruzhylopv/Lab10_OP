class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

    def __repr__(self):
        return f'[{self.data}, {str(self.next)}]'
def stringify(node):
    s = ''
    while node is not None:
        value = node.data
        node = node.next
        s += str(value) + ' -> '
    return s + 'None'

def push(head, data):
    # Your code goes here.
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    chained = None
    for i in range(3, 0, -1):
        chained = push(chained, i)
    return chained

chained = None
chained = push(chained, 3)
chained = push(chained, 2)
chained = push(chained, 1)
print(stringify(push(chained, 8)))

print(stringify(build_one_two_three()))