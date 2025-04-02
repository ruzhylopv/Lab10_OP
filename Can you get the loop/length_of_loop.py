# Інтуїтивно:
#     Ітеруюсь по Linked list

#     Ітеруюсь по хешмапі і присвоюю кожній записаній ноді +1
#     (Це значить що я пройшов від тієї ноди відстань +1)

#     Якщо Я вже відвідав ноду:
#         Зупинити ітерацію. Цикл знайдено
#         Повернути значення хешмап[нода]

#     Якщо не відвідав:
#         записати у hashmap і присвоїти ключу цієї ноди значення 0

def loop_size(node):
    slow = node
    fast = node
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            while True:
                cnt = 0
                while True:
                    slow = slow.next
                    cnt += 1
                    if slow == fast:
                        return cnt
