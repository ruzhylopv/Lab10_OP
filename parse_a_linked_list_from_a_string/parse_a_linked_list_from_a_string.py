class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    s = s.split(' -> ')
    head = Node(int(s.pop(0)))
    probe = head
    for el in s:
        probe.next = Node(el)
        probe = probe.next
    return head
