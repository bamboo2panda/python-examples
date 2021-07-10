class Node:
    """Определяем класс узла с левыми и правыми дочерними узлами"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(" + str(self.value) + ")"


def devider(func):
    def wrapper(*args, **kwargs):
        print('~~~~~~~~~')
        func(*args, **kwargs)
        print('~~~~~~~~~')
    return wrapper


def walk(tree):
    """Рекурсивный способ обхода дерева"""
    if tree is not None:
        print(tree)
        walk(tree.left)
        walk(tree.right)

@devider
def walk2(tree, stack):
    """Итерративный способ обхода дерева"""
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)

my_tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))

walk(my_tree)
walk2(my_tree, [])

