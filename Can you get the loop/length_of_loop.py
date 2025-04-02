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
    hashmap = {node: 0}
    while True:
        node = node.next
        for n in hashmap:
            hashmap[n] += 1

        if node in hashmap:
            return hashmap[node]
        hashmap[node] = 0