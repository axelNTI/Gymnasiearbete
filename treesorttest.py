VALUE = 0
LEFT = 1
RIGHT = 2


def find(tree, num):
    if not tree:
        return
    node = tree[0]
    while num != node[VALUE]:
        i = node[RIGHT if num > node[VALUE] else LEFT]  # index of child
        if i == 0:  # no child in that direction
            return node
        node = tree[i]
    return node


def insert(tree, num):
    if tree:
        node = find(tree, num)
        if num == node[VALUE]:
            return
        node[RIGHT if num > node[VALUE] else LEFT] = len(tree)
    tree.append([num, 0, 0])


numbers = [7, 2, 13, 0, 10, 15, 4, 1, 3, 8]
tree = []
for num in numbers:
    insert(tree, num)
print(tree)
